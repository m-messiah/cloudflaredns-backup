CloudFlare DNS to RFC1035 converter 
===================================


.. image:: https://img.shields.io/pypi/v/cloudflaredns-backup.svg?style=flat-square
    :target: https://pypi.python.org/pypi/cloudflaredns-backup
    


.. image:: https://img.shields.io/pypi/dm/cloudflaredns-backup.svg?style=flat-square
        :target: https://pypi.python.org/pypi/cloudflaredns-backup


Simple tool for backing up your CloudFlare hosted DNS records in format acceptable by BIND (RFC1035)

Installation
------------

.. code:: bash

    pip install cloudflaredns-backup

Usage
-----

*   get all your CloudFlare zones to console

    .. code:: bash

        cf-backup root@example.com 1234567890

*   get only example.com and example2.com zones

    .. code:: bash

        cf-backup root@example.com 1234567890 -z example.com -z example2.com
    
    This example may be simplified as:
    
    .. code:: bash

        cf-backup root@example.com 1234567890 -z "example1.com example2.com"

*   Get only example.com, create if not exists folder and write zone to ./zones/example.com

    .. code:: bash

        cf-backup root@example.com 1234567890 -z example.com -o zones

