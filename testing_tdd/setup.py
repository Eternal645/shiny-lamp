from setuptools import setup, find_packages

setup(
    name = "ndfl-calculator001",
    version = "0.0.1",
    description="Калькулятор НДФЛ по прогрессивной шкале РФ (2025)",
    long_description=open("README.md", encoding="utf-8").read(),
    url="https://github.com/Eternal645/shiny-lamp/tree/feature/ndfl-calculator001-package",
    long_description_content_type = "text/markdown",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    author = "Aleksandr Bagaev"
)