#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
import re


long_description = open("README.md", "r").read()


mainFile = open("sonarrnotification/__main__.py", "r").read()
__version__ = re.search('__version__ = "([^"]+)"', mainFile).group(1)
__description__ = re.search('__description__ = "([^"]+)"', mainFile).group(1)


install_requires = [
    "pyyaml",
    "click",
    "requests"
]


setuptools.setup(
    name="SonarrNotification",
    version=__version__,
    author="Canoziia",
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/canoziia/SonarrNotification",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "snotif=sonarrnotification.__main__:main",
        ]
    },
)
