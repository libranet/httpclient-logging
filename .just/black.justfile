# See ../justfile


# show which black is used
[group: 'black']
black-which:
	@ which black


# run black on python-files
[group: 'black']
black: black-which
	- black docs/ src/ tests/

