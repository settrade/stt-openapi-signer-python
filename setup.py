from setuptools import setup

setup(
    name='stt-openapi-signer',
    version='0.0.1',
    description='Settrade OpenAPI parameters signer',
    license='MIT',
    packages=['stt.openapi'],
    author='Theerapat Chawannakul',
    author_email='theerapatcha@gmail.com',
    keywords=['settrade', 'STT', 'openapi', 'api'],
    install_requires=[
        'ECPy>=1.0.0'
    ],
    url='https://github.com/theerapatcha/stt-openapi-signer-python'
)
