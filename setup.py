#!/usr/bin/env python

from setuptools import setup, find_packages
import sys
import configparser
import os.path

if sys.version_info < (3,):
    print("bitcoin-arbitrage requires Python version >= 3.0")
    sys.exit(1)

setup(name='bitcoin-arbitrage',
      packages=find_packages(),
      version='0.3',
      description='Bitcoin arbitrage opportunity watcher',
      install_requires=[
          "sleekxmpp", 'tenacity', 'pika', 'PyYAML', 'requests', 'pycrypto'
      ],
      arbitrage=['bin/bitcoin-arbitrage'],
      test_suite='nose.collector',
      tests_require=['nose']
      )


if not os.path.isfile("config"):
    config = configparser.ConfigParser()
    config.read('config_template')
    with open('config', 'w') as configfile:
        config.write(configfile)