from distutils.core import setup
from os.path import join, dirname

setup(
    name='cloudflaredns-backup',
    version="1.7.3",
    packages=['cloudflaredns_backup'],
    url='https://github.com/m-messiah/cloudflaredns-backup',
    license='MIT',
    author='m_messiah',
    author_email='m.muzafarov@gmail.com',
    description='CloudFlare DNS backup to BIND files',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    scripts=['scripts/cf-backup'],
    install_requires=['requests'],
    keywords='cloudflare dns backup',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: System Administrators',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
