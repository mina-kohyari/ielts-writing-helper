from setuptools import setup, find_packages
from pathlib import Path

# Read README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="ielts-writing-helper",  # must be unique on PyPI
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ielts=ielts_helper.cli:main"  # creates 'ielts' command
        ]
    },
    description="A CLI tool to help IELTS students improve writing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    author="Your Name",
    url="https://github.com/mina-kohyari/ielts-writing-helper",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)