'''Zephyr
'''

import os
from distutils.core import setup
from setuptools import find_packages

CLASSIFIERS = [
'Development Status :: 3 - Alpha',
'Intended Audience :: Developers',
'Intended Audience :: Science/Research',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python',
'Topic :: Scientific/Engineering',
'Topic :: Scientific/Engineering :: Mathematics',
'Topic :: Scientific/Engineering :: Physics',
'Operating System :: Microsoft :: Windows',
'Operating System :: POSIX',
'Operating System :: Unix',
'Operating System :: MacOS',
'Natural Language :: English',
]

with open('README.md') as fp:
    LONG_DESCRIPTION = ''.join(fp.readlines())

setup(
    name = 'zephyr-seis',
    version = '0.1.7',
    packages = find_packages(),
    install_requires = ['numpy>=1.7',
                        'scipy>=0.13',
                        'click',
                        'galoshes>=0.2.2',
                        'problemo>=0.2.0',
                        'pygeo>=0.1.0',
                        'SimPEG',
                        'future',
                       ],
    author = 'Brendan Smithyman',
    author_email = 'brendan@bitsmithy.net',
    description = 'zephyr',
    long_description = LONG_DESCRIPTION,
    license = 'MIT',
    keywords = 'full-waveform inversion',
    # url = '',
    download_url = 'http://github.com/uwoseis/zephyr',
    classifiers = CLASSIFIERS,
    platforms = ['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
    use_2to3 = False,
    entry_points = {'console_scripts': ['zephyr = zephyr.frontend.cli:zephyr']},
)
