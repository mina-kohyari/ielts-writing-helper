from setuptools import setup, find_packages
from pathlib import Path

# Read README.md safely (Windows friendly)
this_directory = Path(__file__).parent
readme_path = this_directory / "README.md"

long_description = ""
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")

setup(
    name="ielts-writing-helper",  # change if PyPI name is taken
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ielts=ielts_helper.cli:main"
        ]
    },
    description="A CLI tool to help IELTS students improve writing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    url="https://github.com/your-username/ielts-writing-helper",
    license="MIT",
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)