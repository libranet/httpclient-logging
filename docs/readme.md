[![Testing](https://img.shields.io/github/actions/workflow/status/libranet/httpclient-logging/testing.yaml?branch=main&longCache=true&style=flat-square&label=tests&logo=GitHub%20Actions&logoColor=fff")](https://github.com/libranet/httpclient-logging/actions/workflows/testing.yaml)
[![Linting](https://img.shields.io/github/actions/workflow/status/libranet/httpclient-logging/linting.yaml?branch=main&longCache=true&style=flat-square&label=linting&logo=GitHub%20Actions&logoColor=fff")](https://github.com/libranet/httpclient-logging/actions/workflows/linting.yaml)
[![Read the Docs](https://readthedocs.org/projects/httpclient-logging/badge/?version=latest)](https://httpclient-logging.readthedocs.io/en/latest/)
[![Codecov](https://codecov.io/gh/libranet/httpclient-logging/branch/main/graph/badge.svg?token=LYGLIDTNVX)](https://codecov.io/gh/libranet/httpclient-logging)
[![PyPi Package](https://img.shields.io/pypi/v/httpclient-logging?color=%2334D058&label=pypi%20package)](https://pypi.org/project/httpclient-logging/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/libranet/httpclient-logging/blob/main/docs/license.md)


## Installation



Install via pip:

```bash
> bin/pip install httpclient-logging
```

Install via uv:

```bash
> uv add httpclient-logging
```

Install via poetry:

```bash
> poetry add httpclient-logging
```


## Usage

The only thing left to do for you is the create a ``.env`` in the root of your project.


## Registered sitecustomize-entrypoint


The ``httpclient_logging.entrypoint``-function is registered as a ``sitecustomize``-entrypoint in our pyproject.toml_:

via uv:
``` toml
    [project.entry-points."sitecustomize"]
    httpclient_logging = "httpclient_logging.patch:configure"
```

via poetry:
``` toml
    [tool.poetry.plugins]
    [tool.poetry.plugins."sitecustomize"]
    httpclient_logging = "httpclient_logging:entrypoint"
```

Sitecustomize and all its registered entrypoints will be executed at the start of *every* python-process.
For more information, please see [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)


## Compatibility

 [![Python Version](https://img.shields.io/pypi/pyversions/httpclient-logging?:alt:PyPI-PythonVersion)](https://pypi.org/project/httpclient-logging/)
 [![PyPI - Implementation](https://img.shields.io/pypi/implementation/httpclient-logging?:alt:PyPI-Implementation)](https://pypi.org/project/httpclient-logging/)

``httpclient-logging``  works on Python 3.8+, including PyPy3. Tested until Python 3.13,


## Notable dependencies

- [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)
