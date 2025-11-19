"""
Setup configuration for DNA Sequence Analyzer.
"""

from setuptools import setup, find_packages
import os

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="dna-sequence-analyzer",
    version="1.0.0",
    author="Gabriele Iacopo Langellotto",
    author_email="support@dna-sequence-analyzer.dev",
    description="A comprehensive web application for DNA sequence analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GIL794/dna-sequence-analyzer",
    project_urls={
        "Bug Reports": "https://github.com/GIL794/dna-sequence-analyzer/issues",
        "Documentation": "https://github.com/GIL794/dna-sequence-analyzer/tree/main/docs",
        "Source": "https://github.com/GIL794/dna-sequence-analyzer",
        "Changelog": "https://github.com/GIL794/dna-sequence-analyzer/blob/main/CHANGELOG.md",
    },
    packages=find_packages(exclude=["tests", "tests.*", "docs", "data"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dna-analyzer=app:main",
        ],
    },
    keywords=[
        "bioinformatics",
        "dna",
        "sequence-analysis",
        "genomics",
        "molecular-biology",
        "gc-content",
        "orf-detection",
        "primer-design",
        "streamlit",
        "biopython",
    ],
    include_package_data=True,
    zip_safe=False,
)
