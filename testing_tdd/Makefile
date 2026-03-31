install:
	pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ ndfl-yakorolmira

build:
	rm -rf dist/
	python -m build

upload:
	python -m twine upload --repository testpypi dist/*