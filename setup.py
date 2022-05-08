# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from os import path
from setuptools import setup, find_packages

from br4nch import __version__


with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name="br4nch",
    version=__version__,
    description="Data Structure Tree Builder for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TRSTN4/br4nch",
    author="TRSTN4",
    author_email="<tristan@trstn4.com>",
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7"],
    keywords=["br4nch", "python", "python3", "data", "structure", "tree", "builder", "generate", "algorithm"],
    license="GNU General Public License v3.0",
    download_url="https://github.com/TRSTN4/br4nch/archive/refs/tags/" + __version__ + ".tar.gz",
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.7'
)
