venv:
	python -m venv .venv

install: venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip install -e .

test:
	.venv/bin/pytest tests/

lint:
	.venv/bin/flake8 src/ tests/

typecheck:
	.venv/bin/mypy src/

docs:
	python -m pydoc -w ndfl.calculator