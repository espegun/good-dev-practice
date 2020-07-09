from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Only the three first of the below are required.
setup(
    name="Print a DataFrame",
    version="1.0",
    packages=find_packages(),
    install_requires=["pandas"],
    description="Print df",
    long_description=long_description,
    long_description_content_type="text/markdown",
)

