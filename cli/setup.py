import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


long_description = read('README.md') if os.path.isfile("README.md") else ""

setup(
    name='iotex-etl',
    version='1.0.0',
    author='Evgeny Medvedev',
    author_email='evge.medvedev@gmail.com',
    description='Tools for exporting IoTeX blockchain data to JSON',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blockchain-etl/iotex-etl',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='IoTeX',
    python_requires='>=3.6.0,<3.8.0',
    install_requires=[
        'blockchain-etl-common==1.3.0',
        'requests==2.20.0',
        'python-dateutil==2.7.0',
        'click==7.0',
        'pycryptodome==3.9.8',
        'eth-hash==0.2.0',
        'bech32==1.2.0',
        'protobuf==3.12.2',
        'grpcio==1.30.0'
    ],
    extras_require={
        'streaming': [
            'timeout-decorator==0.4.1',
            'google-cloud-pubsub==0.39.1',
        ],
        'dev': [
            'pytest~=4.3.0',
            'pytest-timeout~=1.3.3'
        ],
    },
    entry_points={
        'console_scripts': [
            'iotexetl=iotexetl.cli:cli',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/blockchain-etl/iotex-etl/issues',
        'Source': 'https://github.com/blockchain-etl/iotex-etl',
    },
)
