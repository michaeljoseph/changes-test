import re
from setuptools import setup

init_py = open('changes_test/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", init_py))
metadata['doc'] = re.findall('"""(.+)"""', init_py)[0]

setup(
    name='changes_test',
    version=metadata['version'],
    description=metadata['doc'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    packages=['changes_test'],
    include_package_data=True,
    install_requires=[
        'click < 2.1.0'
    ],
    entry_points={
        'console_scripts': [
            'changes_test = changes_test.cli:main',
        ],
    },
    test_suite='nose.collector',
    license=open('LICENSE').read(),
)

