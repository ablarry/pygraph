PYTHON = python3

help:
	@echo "Commands:"
	@echo "\tmake install\t Install dependencies."
	@echo "\tmake test\t Run tests"
	@echo "\tmake linter\t Linter"

install:
	@echo "Make: install"
	pip install -r requirements.txt

tests:
	${PYTHON} -m unittest discover  -v

linter:
	flake8 ./pygraph/ ./test/
