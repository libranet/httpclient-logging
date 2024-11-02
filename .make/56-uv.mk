# See ../makefile


.PHONY: uv-create-venv  ## create the virtualenv
uv-create-venv:
	uv venv --seed


.PHONY: uv-pip-install  ## run uv install to create the virtualenv
uv-pip-install:
	uv pip install --editable .


.PHONY: uv-pip-install-no-dev  ## run uv install without dev-dependencies
uv-pip-install-no-dev:
	uv pip install --no-dev


.PHONY: uv-sync  ## run uv sync
uv-sync:
	uv sync


.PHONY: uv-lock  ## run uv lock
uv-lock:
	uv lock


.PHONY: uv-lock-upgrade  ## run uv lock --upgrade
uv-lock-upgrade:
	uv lock --upgrade


.PHONY: uv-build  ## run uv build to create the python-package
uv-build:
	uv build --out-dir var/dist


.PHONY: uv-publish  ## publish the package to pypi
uv-publish:
	uv publish var/dist/*


.PHONY: uv-export-requirements  ## generate a requirements.txt-file
uv-export-requirements:
	uv export --format requirements-txt --output-file requirements.txt


.PHONY: uv-export-requirements-docs  ## generate a requirements.txt-file for readthedocs
uv-export-requirements-docs:
	uv export --format requirements.txt --only-group docs --without-hashes --output docs/requirements.txt
