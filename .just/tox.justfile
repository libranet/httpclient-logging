# See ../justfile


# show which tox is used
[group: 'tox']
tox-which:
	@ which tox


# run tox
[group: 'tox']
tox: tox-which
	- tox

