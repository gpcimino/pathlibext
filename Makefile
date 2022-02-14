ifdef PYTHON3
    SYSPYTHON:=${PYTHON3}
else
    SYSPYTHON:=python3
endif

VENV_NAME=.venv
VENV_BIN=${VENV_NAME}/bin
VENV_ACTIVATE=${VENV_BIN}/activate
PYTHON=${VENV_BIN}/python3
PIP=${PYTHON} -m pip

ROOT_PATH:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT:=$(shell basename ${ROOT_PATH})
CODE_DIR=src
TEST_DIR=tests

BRANCH:=$(shell git rev-parse --abbrev-ref HEAD)
HASH:=$(shell git rev-parse HEAD)
WHEEL_FILE=${PROJECT}-${VERSION}-py3-none-any.whl



default:
	@echo "Makefile for $(PROJECT) $(SYSPYTHON)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make venv             install the package in a virtual environment'
	@echo '    make test             test with coverage report'
	@echo '    make build            build python package'
	@echo '    make clean            cleanup all temporary files'
	@echo '    make clean-venv       delete local venv'
	@echo '    make clean-build      cleanup artifacts (rpms, wheels)'
	@echo '    make clean-pyc        cleanup python bn files (pyc, pyo) files'
	@echo '    . ${VENV_ACTIVATE}    activate venv'
	@echo
	@echo '    Use PYTHON3 env var to select sys python interpreter'
	@echo

venv: ${VENV_ACTIVATE}

${VENV_ACTIVATE}: setup.cfg
	test -d ${VENV_ACTIVATE} || ${SYSPYTHON} -m venv ${VENV_NAME}
	${PIP} install -U pip
	${PIP} install -U setuptools
	${PIP} install -U wheel
	${PIP} install -e .
	touch ${VENV_ACTIVATE}

test: venv ${VENV_BIN}/coverage
	${VENV_BIN}/coverage run --include=${TEST_DIR}/*.py  -m unittest discover -s ${TEST_DIR}/; \
	${VENV_BIN}/coverage report;

${VENV_BIN}/coverage:
	${PIP} install coverage

clean-venv:
	rm -Rf ${VENV_NAME}

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	rm -f ${PROJECT}*.rpm
	rm -f ${PROJECT}/meta

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

build:
	${PIP} install -U build
	${PYTHON} -m build

test-build:
	mkdir -p testbuild
	${SYSPYTHON} -m venv testbuild/.venvbuild
	testbuild/.venvbuild/bin/python -m pip install "$(shell ls -t -d -1  dist/* | head -n 1)"
	testbuild/.venvbuild/bin/python -c "from pathlib import Path; import pathlibext; print(Path.systmpdir());"
	rm -rf testbuild

testpublish:
	${PIP} install --upgrade twine
	${PYTHON} -m twine upload --config-file "$(shell find ~ -path ./mnt -prune -o -name '.pypirc' -print)" --repository testpypi dist/*.whl

publish:
	${PIP} install --upgrade twine
	${PYTHON} -m twine upload --config-file "$(shell find ~ -path ./mnt -prune -o -name '.pypirc' -print)" --repository pypi dist/*.whl
