from distutils.core import setup

from time import sleep
sleep(10)

setup(
    name='sampledep',
    version='1.0',
    py_modules=['dep'],
)
