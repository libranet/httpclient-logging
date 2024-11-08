# See ../justfile

# show which flake8 is used
[group: 'flake8']
flake8-which:
	@ which flake8


# run flake8 on python-files
[group: 'flake8']
flake8: flake8-which
	- flake8 docs/ src/ tests

