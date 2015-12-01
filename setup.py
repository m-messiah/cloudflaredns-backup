from distutils.core import setup
from os.path import join, dirname

setup(
    name='cloudflaredns-backup',
    version='1.0',
    packages=['cloudflaredns_backup'],
    url='',
    license='',
    author='m_messiah',
    author_email='m.muzafarov@gmail.com',
    description='CloudFlare DNS backup to BIND files',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)
