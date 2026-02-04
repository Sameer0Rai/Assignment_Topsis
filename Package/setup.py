from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="Topsis-Sameer-102303773",
    version="1.0.2",
    author="Sameer Rai",
    author_email="srai1_be23@thapar.edu",
    description="A Python package implementing the TOPSIS method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
)
