'''
https://python-packaging.readthedocs.io/en/latest/minimal.html
'''

from setuptools import setup

setup(name='LazyLoader',
      version='1.0',
      description='Lazy loader',
      url='https://github.com/joreeves/LazyLoader',
      author='Tensorflow',
      author_email='',
      license='MIT',
      packages=['lazyloader'],
      install_requires=['__future__', 'importlib', 'types', 'logging']
      zip_safe=False)