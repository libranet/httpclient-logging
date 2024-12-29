# See ../justfile


# show which pytest is used
[group: 'pytest']
pytest-which:
	@ which pytest


# run pytest on python-files
[group: 'pytest']
pytest:
	- pytest tests


# run pytest on python-files with the --pdb-flag
[group: 'pytest']
pytest-pdb:
	- pytest tests --pdb


# run pytest and generate html-coverage --pdb-flag
[group: 'pytest']
pytest-cov:
	- pytest tests --cov=src --cov-report html  --cov-report xml --cov-report term  -v


# run pytest with the --pdb-flag and generate html-coverage
[group: 'pytest']
pytest-pdb-cov:
	- pytest tests --cov=src --cov-report html  --cov-report xml --cov-report term  -v  --pdb


# run pytest with the --pdb-flag and generate html-coverage
[group: 'pytest']
pytest-cov-pdb: pytest-pdb-cov


# run pytest with the --pdb-flag and generate html-coverage on last failed tests
[group: 'pytest']
pytest-pdb-cov-lf:
	- pytest tests --cov=src --cov-report html -v --pdb --lf
