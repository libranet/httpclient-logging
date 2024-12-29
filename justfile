# Just is a crossplatform task-runner, similar to make.
# And justfiles are equivalent to makefiles.
#
# Official docs:
#  - https://just.systems/man/en
#
# Usage:
#   > just --help
#   > just <taskname>
#
# Notes:
#  - Comments immediately preceding a recipe will appear in just --list:# Just is a crossplatform task-runner, similar to make.
# And justfiles are equivalent to makefiles.
#
# Official docs:
#  - https://just.systems/man/en
#
# Usage:
#   > just --help
#   > just <taskname>
#
# Notes:
#  - Comments immediately preceding a recipe will appear in just --list:

# load environment variables from .env file
# set dotenv-filename := ".env"
set dotenv-load	:= true

# search for justfiles in parent directories
set fallback

# set tempdir := "var/tmp"

# set shell to powershell on Windows
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]
set shell := ["bash", "-uc"]

import '.just/black.justfile'
import '.just/dir-structure.justfile'
import '.just/dotenv.justfile'
import '.just/flake8.justfile'
import '.just/git.justfile'
import '.just/ipython.justfile'
import '.just/isort.justfile'
import '.just/mypy.justfile'
import '.just/nox.justfile'
import '.just/pre-commit.justfile'
import '.just/pylint.justfile'
import '.just/pyroma.justfile'
import '.just/pytest.justfile'
import '.just/readthedocs.justfile'
import '.just/ruff.justfile'
import '.just/sphinx.justfile'
import '.just/tox.justfile'
import '.just/uv.justfile'

# Help target
help:
    @ just --list --unsorted
