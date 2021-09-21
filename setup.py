#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_lucafs',
      version = '0.1',
      packages = ['dev_aberto'],
      author = 'Luca Farah',
      plataforms = ['Windowns', 'Linux' , 'Unix' , 'MAC OS'],
      python_requires=">=3.6",
      install_requires=["requests"],
      scripts=['scripts/hello.py']
      )