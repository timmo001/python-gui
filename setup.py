#!/usr/bin/env python
import io
import os

from setuptools import find_packages, setup


def find(name, path):
    for root, dir, files in os.walk(path):
        print(f"{root} : {dir} : {files}")
        if name in files:
            return os.path.join(root, name)


# Get packages from requirements.txt
with io.open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

# Get version from version.txt
with io.open("version.txt", encoding="utf-8") as f:
    version = f.read()

print(version)

setup(
    name="pythongui",
    version=version,
    description="Python GUI",
    keywords="python gui",
    author="Aidan Timson (Timmo)",
    author_email="contact@timmo.xyz",
    license="MIT",
    url="https://github.com/timmo001/python-gui",
    packages=find_packages(exclude=["tests", "generator"]),
    install_requires=requirements,
)
