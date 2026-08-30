# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module httpclient_logging.patch."""

import logging
import os

import freezegun
import urllib3


def test_invalid_httpclient_debuglevel(caplog, default_httpclient):
    from httpclient_logging.patch import set_httpclient_debuglevel

    # Set the logging level to capture warnings
    caplog.set_level(logging.WARNING)

    set_httpclient_debuglevel(debuglevel="foo")

    # Check if the warning log message is captured
    assert "Cannot change http.client.HTTPConnection.debuglevel: foo is not an integer." in caplog.text


def test_httpclient_debuglevel(default_httpclient):
    import http.client

    from httpclient_logging.patch import set_httpclient_debuglevel

    # implicit default
    assert http.client.HTTPConnection.debuglevel == 0

    # explicit default
    os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "0"
    set_httpclient_debuglevel()
    assert http.client.HTTPConnection.debuglevel == 0

    os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "1"
    set_httpclient_debuglevel()
    assert http.client.HTTPConnection.debuglevel == 1


def test_configure():
    import http.client
    import typing

    from httpclient_logging.patch import configure, undo

    # ``http.client.print`` is a runtime monkeypatch; view it as ``Any`` for the type-checkers.
    http_client: typing.Any = http.client

    configure()
    assert http.client.HTTPConnection.debuglevel == 1
    assert http_client.print.__name__ == "<lambda>"

    undo()
    assert http.client.HTTPConnection.debuglevel == 0
    assert http_client.print.__name__ == "print"


def test_unpatched_httpclient_print(capsys, debuglevel_1, http_manager, url):
    from httpclient_logging.patch import set_httpclient_debuglevel, unpatch_httpclient_print

    assert os.getenv("DEBUGLEVEL_HTTPCONNECTION") == "1"

    set_httpclient_debuglevel()

    unpatch_httpclient_print()

    _ = http_manager.request("GET", url, timeout=3)
    # send: b'GET / HTTP/1.1\r\nHost: example.com\r\n
    #     Accept-Encoding: identity\r\nUser-Agent: python-urllib3/1.26.14\r\n\r\n'
    # reply: 'HTTP/1.1 200 OK\r\n'
    # header: Age: 407642
    # header: Cache-Control: max-age=604800
    # header: Content-Type: text/html; charset=UTF-8
    # header: Date: Sat, 04 Mar 2023 10:20:18 GMT
    # header: Etag: "3147526947+ident"
    # header: Expires: Sat, 11 Mar 2023 10:20:18 GMT
    # header: Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
    # header: Server: ECS (dcb/7EA3)
    # header: Vary: Accept-Encoding
    # header: X-Cache: HIT
    # header: Content-Length: 1256

    captured = capsys.readouterr()
    assert "send: b'GET / HTTP/1.1\\r\\nHost: example.com" in captured.out
    assert "reply: 'HTTP/1.1 200 OK\\r\\n" in captured.out
    assert "header: " in captured.out
    assert "header: Date:" in captured.out


def test_patched_httpclient_print(caplog, debuglevel_1, http_manager, setup_logging, url):
    from httpclient_logging.patch import patch_httpclient_print, set_httpclient_debuglevel

    assert os.environ["DEBUGLEVEL_HTTPCONNECTION"] == "1"

    set_httpclient_debuglevel()

    caplog.set_level(logging.DEBUG)

    patch_httpclient_print()

    with freezegun.freeze_time("2023-01-01"):
        _ = http_manager.request("GET", url, timeout=3)

    # The patched ``print`` routes every ``http.client`` debug line through ``log.debug``,
    # so each line shows up verbatim in ``caplog.messages``. Assert on the parts that a
    # live ``GET http://example.com`` always produces; header *values* (Date, Server, ...)
    # depend on whatever CDN fronts the site, so only their stable prefixes are checked.
    messages = caplog.messages
    joined = "\n".join(messages)

    assert "Setting http.client.HTTPConnection.debuglevel to 1" in messages
    assert "Starting new HTTP connection (1): example.com:80" in messages
    assert (
        "send: b'GET / HTTP/1.1\\r\\nHost: example.com\\r\\nAccept-Encoding: identity\\r\\n"
        f"User-Agent: python-urllib3/{urllib3.__version__}\\r\\n\\r\\n'"
    ) in messages
    assert "reply: 'HTTP/1.1 200 OK\\r\\n'" in messages

    # header lines: logged one per line, "header: <name>: <value>"
    assert "header: Date: " in joined
    assert "header: Content-Type: text/html" in joined

    # urllib3 connectionpool summary (trailing body length is an int or "None")
    assert 'http://example.com:80 "GET / HTTP/1.1" 200 ' in joined
