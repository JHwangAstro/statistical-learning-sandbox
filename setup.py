""" Repository containing code written while reviewing statistical learning
methods.
"""

import os
from setuptools import setup, find_packages

__author__ = "Jason Hwang"
__email__ = "@".join(("jhwang.astro", "gmail.com"))
__url__ = "https://github.com/JHwangAstro/statistical-learning-sandbox"
__description__ = "Code written to review statistical learning methods."

with open("statlearning/VERSION", "r") as version_file:
    version = version_file.read().strip()

this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

install_requires = [
    "attrs>=20.3.0",
    "numpy>=1.19.5",
    "scipy>=1.5.4"
]

setup(
    name="statlearning_sandbox",
    version=version,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=__email__,
    url=__url__,
    python_requires=">=3.6",
    install_requires=install_requires,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    package_data={"statlearning": ["VERSION"]}
)
