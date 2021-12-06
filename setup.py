from setuptools import setup, find_packages

setup(
    name="br4nch",
    version="1.0.0",
    description="br4nch is a data structure tree generator for Python.",
    url="https://br4nch.com",
    author="TRSTN4",
    author_email="<tristan@trstn4.com>",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Intended Audience :: Developers"
        "Operating System :: Unix"
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"],
    keywords=["br4nch", "python", "python3", "data", "structure", "tree", "generate", "algorithm"],
    license="GNU General Public License v3.0",
    download_url="https://github.com/TRSTN4/br4nch/archive/refs/tags/v1.0.0.tar.gz",
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3'
)
