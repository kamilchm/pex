# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'CHANGES.rst')) as fp:
  LONG_DESCRIPTION = fp.read()


setup(
  name = 'pex',
  version = '0.7.0',
  description = "The PEX packaging toolchain.",
  long_description = LONG_DESCRIPTION,
  url = 'https://github.com/pantsbuild/pex',
  license = 'Apache License, Version 2.0',
  zip_safe = True,
  classifiers = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
  ],
  packages = [
      'pex',
      'pex.bin',
      'pex.http',
  ],
  install_requires = [
    'setuptools>=2.2',
  ],
  tests_require = [
    'mock',
    'twitter.common.contextutil>=0.3.1,<0.4.0',
    'twitter.common.lang>=0.3.1,<0.4.0',
    'twitter.common.testing>=0.3.1,<0.4.0',
    'twitter.common.dirutil>=0.3.1,<0.4.0',
    'pytest',
  ],
  entry_points = {
    'console_scripts': [
      'pex = pex.bin.pex:main [whl]',
    ],
  },
  extras_require = {
    'whl': ['wheel>=0.24.0,<0.25.0'],
  },
)
