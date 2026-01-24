# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module httpclient_logging.about."""

import packaging.version


def test_version() -> None:
    from httpclient_logging.about import version

    assert isinstance(version, str)
    assert packaging.version.parse(version) >= packaging.version.parse("0.0")


def test_license() -> None:
    from httpclient_logging.about import license_

    assert isinstance(license_, str)
    assert "Copyright" in license_
