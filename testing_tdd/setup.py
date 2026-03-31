from setuptools import setup, find_packages

setup(
    name = "ndfl-yakorolmira",
    version = "0.0.0",
    long_description = "Tax calculator",
    long_description_content_type = "text/markdown",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    author = "Aleksandr Bagaev"
)