# See ../justfile


# show which isort is used
[group: 'isort']
isort-which:
	@ which isort


# run isort on python-files
[group: 'isort']
isort: isort-which
	- isort --settings-path=pyproject.toml src/**/*.py tests/**/*.py