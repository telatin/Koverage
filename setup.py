import os
from setuptools import setup, find_packages


def get_version():
    with open(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "koverage",
            "koverage.VERSION",
        )
    ) as f:
        return f.readline().strip()
    

def get_description():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description


def get_data_files():
    data_files = [(".", ["README.md"])]
    return data_files


CLASSIFIERS = [
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT license",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

setup(
    name="koverage",
    packages=find_packages(),
    url="https://github.com/beardymcjohnface/Koverage",
    python_requires=">=3.7",
    description="Quickly get coverage statistics given reads and an assembly",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    version=get_version(),
    author="Michael Roach",
    author_email="beardymcjohnface@gmail.com",
    data_files=get_data_files(),
    py_modules=["koverage"],
    install_requires=[
        "snakemake>=7.14.0",
        "pyyaml>=6.0",
        "Click>=8.1.3",
        "attrmap>=0.0.7",
        "zstandard>=0.21.0",
        "numpy>=1.24.3",
    ],
    entry_points={
        "console_scripts": [
            "koverage=koverage.__main__:main"
        ]
    },
    include_package_data=True,
)
