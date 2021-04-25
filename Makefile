PYTHON = python3

help:
	@echo "Commands:"
	@echo "\tmake install\t Install dependencies."
	@echo "\tmake test\t Runit tests"

install:
	@echo "Make: install"
	pip install -r requirements.txt

tests:
	${PYTHON} -m unittest discover  -v
