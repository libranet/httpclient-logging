# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
"""conftest.py - custom pytest-plugins.

For more information about conftest.py, please see:

 - https://docs.pytest.org/en/latest/writing_plugins.html
 - https://pytest-flask.readthedocs.io/en/latest/tutorial.html
 - https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files

This file contains the configurations that we need for running our tests:

 - different data, dummy, regression, classification
 - libpaths to the different models we want to test
 - A sample (baseline) configuration to pass to the experiment and artifact object
 - Utilities for generating new configurations based on provided parameters (model type, problem type)


Note: The tests-directory itself is NOT a python-package (no __init__.py).
Please avoid putting an __init.py-file in this directory. If you by accident put an __init__.py in this tests-directory,
you will not be able to run pytest, instead it will fail with:

    > ImportError: Error importing plugin "_helpers": No module named '_helpers'

The "_helpers"-directory contains code that can be re-used in various tests.

Usage:
======
  # run all test from the toplevel-directory:
  > pytest tests

  # to display the full list of tests being run
  > pytest tests -vv

  # run tests, but stop in interactive debugger upon every failure
  > pyest tests --pdb

  # run only tests-modules  filtered in a glob
  > pytest tests/foo/test_bar*

  # run only specific tests inside specific modules
  > pytest  tests/test_foo/test_bar*::*test_baz

  # only run tests with a certain marker
  > pytest -v -m "integration"
  > pytest -v -m "not integration"

  # generate coverage in the terminal + in html-report
  > pytest --cov="autoread_dotenv"  --cov-report=term  --cov-report=html

"""

import importlib
import logging
import os
import urllib3

import pytest

import httpclient_logging

# reload modules to ensure proper coverage because
# this code has already been executed by sitecustomize
importlib.reload(httpclient_logging)
importlib.reload(httpclient_logging.patch)


@pytest.fixture
def debuglevel_0():
    os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "0"


@pytest.fixture
def debuglevel_1():
    os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "1"


@pytest.fixture
def http():
    http_ = urllib3.PoolManager()
    return http_


@pytest.fixture
def url():
    return "http://example.com"


@pytest.fixture
def setup_logging():
    logging.basicConfig(
        encoding="utf-8",
        # format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        # datefmt='%H:%M:%S',
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)-7s - %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )

    console = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)-7s - %(message)s")
    console.setFormatter(formatter)
    console.setLevel(logging.DEBUG)

    log = logging.getLogger()
    log.addHandler(console)
    return log
