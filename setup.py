import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

#TODO: handle simplejson for python < 2.6
setup(
    name = 'python-tastypie-client',
    version = '0.1',
    packages = ['tastypie_client'],
    include_package_data = True,
    license = 'BSD License - see LICENSE file', 
    description = 'A client library for talking to HATEOAS REST apis created by django tastypie',
    long_description = README,
    author = 'Kenneth Knowles; Mark Redar',
    author_email = 'http://kennknowles.com; mredar@gmail.com',
    url = 'https://github.com/mredar/python-tastypie-client',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
	'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [
        'httplib2',
        ],
)

