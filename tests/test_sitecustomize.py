# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module sitecustomize."""


def test_import_sitecustomize() -> None:
    try:
        import sitecustomize  # noqa: F401
    except ImportError as exc:
        # package sitecustomize-entrypoints is not installed
        msg = "Can not import sitecustomize. Package sitecustomize-entrypoints not installed?"
        raise AssertionError(msg) from exc


def test_entrypoint_registration() -> None:
    from sitecustomize._vendor.importlib_metadata import entry_points

    assert "httpclient_logging" in entry_points(group="sitecustomize").names
