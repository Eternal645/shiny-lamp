from setuptools import setup, find_packages

setup(
    name = "ndfl-calculator001",
    version = "0.0.1",
    long_description = "НДФЛ калькулятор для физических лиц, работающих по трудовому договору, для расчета налогов и взносов в России.",
    long_description_content_type = "text/markdown",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    author = "Aleksandr Bagaev"
)