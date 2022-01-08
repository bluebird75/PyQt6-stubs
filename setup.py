"""Python setup script.

:author: Stefan Lehmann <stlm@posteo.de>
:license: MIT, see license file or https://opensource.org/licenses/MIT

:created on 2018-10-06 10:55:36
:last modified by: Stefan Lehmann
:last modified time: 2019-07-23 10:27:04

"""
import io
import os
import re
from setuptools import setup


def read(*names, **kwargs):
    try:
        with io.open(
            os.path.join(os.path.dirname(__file__), *names),
            encoding=kwargs.get("encoding", "utf8")
        ) as fp:
            return fp.read()
    except IOError:
        return ''


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = read('README.md')


setup(
    name="PyQt6-stubs",
    url="https://github.com/bluebird75/PyQt6-stubs",
    author="Stefan Lehmann",
    maintainer="Kyle Altendorf, Bryce Beagle, Florian Bruhin, Philippe Fre;y",
    maintainer_email="phil.fremy@free.fr",
    description="PEP561 stub files for the PyQt6 framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=find_version('PyQt6-stubs', '__init__.pyi'),
    python_requires=">= 3.6",
    package_data={"PyQt6-stubs": ['*.pyi']},
    packages=["PyQt6-stubs"],
    extras_require={
        "dev": ["mypy", "pytest"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development"
    ]
)
