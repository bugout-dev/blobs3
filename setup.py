from setuptools import find_packages, setup

with open("blobs3/version.txt") as ifp:
    VERSION = ifp.read().strip()

long_description = ""
with open("README.md") as ifp:
    long_description = ifp.read()

setup(
    name="blobs3",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "boto3",
        "fastapi",
        "pydantic",
        "web3",
    ],
    extras_require={
        "dev": ["black", "mypy", "isort"],
        "distribute": ["setuptools", "twine", "wheel"],
    },
    description="blobs3: Blob storage with web3 access control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Moonstream",
    author_email="engineering@moonstream.to",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "blobs3=blobs3.cli:main",
        ]
    },
    package_data={"blobs3": ["version.txt"]},
    include_package_data=True,
)
