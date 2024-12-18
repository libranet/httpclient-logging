# See ../makefile

# Source .env.example, because .env might not yet exist.
# -include .env.example

# Source .env, if it exists. This Overrides any env-vars sourced in .env.example.
# -include .env


# instantiate the dotenv-file (no override)
# cp --backup  creates .env~, but will overwrite this next time.
# safest way, is to not overwrite existing .env-files, manual intervention needed.
[group: 'dotenv']
dotenv-install-from-example:
	@echo -e "Copying .env.example to .env" ;\
	cp -n .env.example .env ;\
	echo "Please review any credentials in the .env-file."


# replace placeholder __CDW__ with current working directory
[group: 'dotenv']
dotenv-set-basedir:
	@echo -e "Replacing string __CWD__ -> $(PWD)" ;\
	$(SED) -i 's@__CWD__@'"$(PWD)"'@'  .env


# install .env-file from .env.example
[group: 'dotenv']
dotenv-install: dotenv-install-from-example dotenv-set-basedir