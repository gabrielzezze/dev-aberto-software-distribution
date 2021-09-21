#!/usr/bin/env python3
from setuptools import setup

setup(
    name="dev_aberto_gabrielzezze",
    version="0.1.2",
    packages=["dev_aberto"],
    author="Gabriel Zezze",
    author_email="gabriel@zezze.dev",
    description="Example package for Open development class by Insper",
    long_description="Example package for Open development class by Insper",
    url="https://github.com/gabrielzezze/dev-aberto-software-distribution",
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    python_requires=">=3.6",
    install_requires=["requests", "babel", "python-gettext"],
    scripts=["scripts/hello.py"],
)
