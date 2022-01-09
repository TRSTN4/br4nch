import subprocess
from os import path
from setuptools import setup, find_packages

version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
).split("-")[0]

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name="br4nch",
    version=version,
    description="br4nch is a data structure tree generator for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TRSTN4/br4nch",
    author="TRSTN4",
    author_email="<tristan@trstn4.com>",
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.9"],
    keywords=["br4nch", "python", "python3", "data", "structure", "tree", "generate", "algorithm"],
    license="GNU General Public License v3.0",
    download_url="https://github.com/TRSTN4/br4nch/archive/refs/tags/" + version + ".tar.gz",
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3'
)
