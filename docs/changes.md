# Changelog

All notable changes to this project will be documented in this file.


## Unreleased (YYYY-MM-DD)

## 1.1 (2025-03-13)
- Remove ``httpclient_logging.patch.cancel``-function, since this is now available in ``sitecustomize-entrypoints>=1.1.0``

- Depend on ``sitecustomize-entrypoints>=1.1.0``
-
- Remove range-pinning ``python = ">=3.8.0,<4.0"``, only specify bottom-version ``">=3.8.0"``

- Remove range-pinned dependencies ``tox``, ``nox`` that require us to pin ``python = "<4.0"``


## 1.0 (2023-03-30)

- Refactored and renamed entrypoint into ``autoread_dotenv.entrypoint``.

- Add boilerplate-files to comply with Github's [_Community Standards_](https://github.com/libranet/httpclient-logging/community)

- Test releasing via ``poetry-release``.

- Convert docs from restructured text to markdown.

- Update project-description in pyproject.toml. [WouterVH]

- Add ``readthedocs.yaml``.

- Package created by [Wouter Vanden Hove <wouter@libranet.eu>]
