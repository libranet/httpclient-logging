# See ../justfile


# show which nox is used
[group: 'nox']
nox-which:
	@ which nox


# run nox
[group: 'nox']
nox: nox-which
	- nox
