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

        cf-backup root@example.com 1234567890 # args
        CF_EMAIL=root@example.com CF_TOKEN=1234567890 cf-backup # env
        echo "root@example.com:1234567890" > credentials.cfg && cf-backup -c credentials.cfg # config file

*   get only example.com and example2.com zones (here and other - just args examples. ENV and cred-file are same)

    .. code:: bash

        cf-backup root@example.com 1234567890 -z example.com -z example2.com
    
    This example may be simplified as:
    
    .. code:: bash

        cf-backup root@example.com 1234567890 -z "example1.com example2.com"

*   Get only example.com, create if not exists folder and write zone to ./zones/example.com, and write NS in zone

    .. code:: bash

        cf-backup root@example.com 1234567890 -z example.com -o zones --ns ns.example.com

CHANGELOG
---------

+   v1.7.4
    Real SERIAL number for zones (last modified time in format YYYYmmddHH)
+   v1.7.3
    Remove "Exported date" for sensitive tracking of zone-file (for example in Git)
+   v1.7.2
    Possibility to add custom name servers for simplify backup deploy of zone.
+   v1.6
    Add possibility to determine credentials in args/environment/file
+   v1.5
    Small bug fixes
+   v1.4
    Fix for unicode support in Python3
+   v1.3
    Fix for unicode support in Python2
+   v1.2
    Fix for NoneType objects
+   v1.1
    Python2 support
+   v1.0b
    PyPI package
+   v1.0a
    Python2-3 cloudflare backup tool
