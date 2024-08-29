# File: setup.py
from setuptools import setup, find_packages

setup(
    name="readme-md-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "jinja2",
    ],
    entry_points={
        "console_scripts": [
            "generate-readme=readme_md_generator.cli:main",
        ],
    },
    author="Likhon Sheikh",
    author_email="me@likhonsheikh.com",
    description="An ultimate GitHub README.md generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/likhonsheikhorg/readme-md-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)