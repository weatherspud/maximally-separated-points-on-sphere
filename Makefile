python_files := $(wildcard *.py)
max_line_length := 100

ve:
	virtualenv $@ --python=python3
	. $@/bin/activate && pip install -r requirements.txt

.PHONY:
pylint: ve
	. ve/bin/activate \
	  && echo $(python_files) \
	  | PYTHONPATH=. xargs pylint --rcfile ./.pylintrc -d missing-docstring

.PHONY: mypy
mypy: ve
	. ve/bin/activate \
	  && echo $(python_files) \
	  | xargs -n 1 mypy --silent-imports --strict-optional --disallow-untyped-defs

.PHONY: pep8
pep8: ve
	. ve/bin/activate \
	  && echo $(python_files) \
	  | xargs pep8 --max-line-length=$(max_line_length)

.PHONY: check
check: pylint pep8 mypy
