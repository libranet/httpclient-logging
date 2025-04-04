# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module httpclient_logging.__init__."""

import packaging.version


def test_version():
    from httpclient_logging import __version__

    assert isinstance(__version__, str)
    assert packaging.version.parse(__version__) >= packaging.version.parse("0.0")


def test_copyright():
    from httpclient_logging import __copyright__

    assert isinstance(__copyright__, str)
    assert "Copyright" in __copyright__


def test_metadata():
    from httpclient_logging import __metadata__

    assert isinstance(__metadata__, dict)
