from setuptools import setup, find_packages

import sys
if sys.version_info < (3,8):
    sys.exit('Sorry, Python < 3.8 is not supported')

setup(
    name='actions',
    extras_require=dict(test=['pytest']),
    packages=find_packages(where='src'),
    packages_dir={"","src"}
)