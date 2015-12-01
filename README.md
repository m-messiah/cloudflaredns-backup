# CloudFlare DNS to Bind converter

Simple tool for backing up your CloudFlare hosted DNS records in format acceptable by BIND

# Usage

+   get all your CloudFlare zones to console
        
        cloudflaredns2bind root@example.com 1234567890

+   get only example.com and example2.com zones
    
        cloudflaredns2bind root@example.com 1234567890 -z example.com -z example2.com

    This example may be simplified as:
    
        cloudflaredns2bind root@example.com 1234567890 -z "example1.com example2.com"

+   Get only example.com, create if not exists folder and write zone to ./zones/example.com
        
        cloudflaredns2bind root@example.com 1234567890 -z example.com -o zones

