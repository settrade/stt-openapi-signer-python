import sys
from setuptools import setup

if sys.version_info >= (3, 0):
    install_requires = ["ECPy >= 1.0.0"]
else:
    install_requires = ["ECPy == 0.8.0"]

setup(
    name='stt-openapi-signer',
    version='0.0.1',
    description='Settrade OpenAPI parameters signer',
    license='MIT',
    packages=['stt', 'stt.openapi'],
    author='Theerapat Chawannakul',
    author_email='theerapatcha@gmail.com',
    keywords=['settrade', 'STT', 'openapi', 'api'],
    install_requires=install_requires,
    url='https://github.com/theerapatcha/stt-openapi-signer-python'
)
