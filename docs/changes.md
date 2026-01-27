# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

- Update `.pre-commit-config.yaml` with additional hooks.

- Update GitHub Actions workflows with pinned versions.

- Add new justfiles: bandit, gh, just, mdformat, prek, release, safety, sshx, ty, ubuntu.

## 1.2 (2025-03-13)

- Remove `docs/requirements`, as we use fully uv

- Add `ty` as type-checking dependency.

## 1.1 (2025-03-13)

- Remove `httpclient_logging.patch.cancel`-function,
  since this is now available in `sitecustomize-entrypoints>=1.1.0`

- Depend on `sitecustomize-entrypoints>=1.1.0`

- Remove range-pinning `python = ">=3.8.0,<4.0"`, only specify bottom-version `">=3.8.0"`

- Remove range-pinned dependencies `tox`, `nox` that require us to pin `python = "<4.0"`

## 1.0 (2023-03-30)

- Refactored and renamed entrypoint into `autoread_dotenv.entrypoint`.

- Add boilerplate-files to comply with Github's [_Community Standards_](https://github.com/libranet/httpclient-logging/community)

- Test releasing via `poetry-release`.

- Convert docs from restructured text to markdown.

- Update project-description in pyproject.toml. [WouterVH]

- Add `readthedocs.yaml`.

- Package created by \[Wouter Vanden Hove <wouter@libranet.eu>\]
