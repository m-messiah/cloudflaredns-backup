from os import makedirs, path
from requests import Session
from datetime import datetime

import logging

__author__ = 'm_messiah'


class CloudFlareDns(object):
    def __init__(self, email, token, zones, ns):
        self.conn = Session()
        self.conn.headers = {
            'X-Auth-Email': email,
            'X-Auth-Key': token,
        }
        self.url = "https://api.cloudflare.com/client/v4/"
        self.zones = self.get_zones(zones)
        self.ns = ns

    def get_pages(self, url):
        result = []
        logging.debug("Fetch %s" % url)
        try:
            resp = self.conn.get(self.url + url)
            if resp.status_code != 200:
                logging.error("Error in fetching. url=%s status_code=%s"
                              % (url, resp.status_code))
                return result
            resp = resp.json()
            if isinstance(resp['result'], dict):
                result = resp['result']
                return result

            result.extend(resp['result'])

            try:
                total_pages = resp['result_info']['total_pages']
            except:
                total_pages = 1
            if total_pages > 1:
                logging.debug("Found %s pages on CloudFlare" % total_pages)
                for page in range(2, total_pages + 1):
                    resp = self.conn.get(self.url + url, params={'page': page})
                    if resp.status_code != 200:
                        logging.error(
                            "Error in fetching. url=%s page=%s status_code=%s"
                            % (url, page, resp.status_code)
                        )
                        break
                    result.extend(resp.json()['result'])
        except Exception as error:
            logging.warning("Error while fetching %s: %s" % (url, error))
        finally:
            return result

    def get_zones(self, zones):
        return {
            zone['name']: {
                'records': self.get_pages("zones/%s/dns_records" % zone['id']),
                'info': self.get_pages("zones/%s" % zone['id'])
            } for zone in self.get_pages("zones")
            if not zones or zone['name'] in zones
        }

    def bindify(self, zone):
        try:
            timestamp = datetime.strptime(
                self.zones[zone]['info']['modified_on'],
                "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            timestamp = datetime.now()

        serial = timestamp.strftime("%Y%m%d%H")
        result = [
            u'$ORIGIN %s.' % zone,
            u"""@\t300\tSOA\t%s. hostmaster.%s. (
                                %s ; Serial
                                28800   ; Refresh
                                7200    ; Retry
                                604800  ; Expire
                                300)    ; Minimum TTL
            """ % (zone, zone, serial),
        ]
        for ns in self.zones[zone]['info']["name_servers"]:
            result.append("         IN NS %s." % ns)

        if self.ns:
            for ns in self.ns:
                result.append("         IN NS %s." % ns)

        for rec in self.zones[zone]['records']:
            content = rec['content']
            if rec['type'] in {'SPF', 'TXT'}:
                content = "\"" + content + "\""
            elif rec['type'] == 'CNAME':
                content += "."
            elif rec['type'] == 'MX':
                content = u'\t'.join((str(rec['priority']), content))
            result.append(u"\t".join((
                rec['name'] + ".",
                "300" if rec['ttl'] == 1 else str(rec['ttl']),
                "IN",
                rec['type'],
                content
            )))
        return u"\n".join(result)


def backup_dns(email, token, zones, output, ns):
    cloudflare = CloudFlareDns(email, token, zones, ns)
    if output:
        try:
            makedirs(output)
        except OSError as exc:
            from errno import EEXIST
            if exc.errno == EEXIST and path.isdir(output):
                pass
            else:
                logging.error("Can't create directory %s" % output)
                exit(1)
        for zone in cloudflare.zones:
            with open(path.join(output, zone), "wb") as bind_file:
                bind_file.write(cloudflare.bindify(zone).encode("utf8"))
    else:
        for zone in cloudflare.zones:
            print(cloudflare.bindify(zone))
            print()
