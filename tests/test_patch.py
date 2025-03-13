# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module httpclient_logging.patch."""

import http.client
import os

import freezegun


def test_httpclient_debuglevel():
    from httpclient_logging.patch import set_httpclient_debuglevel

    # implicit default
    # assert http.client.HTTPConnection.debuglevel == 0
    # explicit default
    os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "0"
    set_httpclient_debuglevel()
    assert http.client.HTTPConnection.debuglevel == 0

    os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "1"
    set_httpclient_debuglevel()
    assert http.client.HTTPConnection.debuglevel == 1


def test_configure():
    from httpclient_logging.patch import configure

    configure()


def test_unpatched_httpclient_print(capsys, debuglevel_1, http, url):  # noqa: ARG001
    from httpclient_logging.patch import set_httpclient_debuglevel, unpatch_httpclient_print

    assert os.environ["DEBUGLEVEL_HTTPCONNECTION"] == "1"

    set_httpclient_debuglevel()

    unpatch_httpclient_print()

    _ = http.request("GET", url, timeout=3)
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


def test_patched_httpclient_print(debuglevel_1, http, url):  # noqa: ARG001
    from httpclient_logging.patch import patch_httpclient_print, set_httpclient_debuglevel

    assert os.environ["DEBUGLEVEL_HTTPCONNECTION"] == "1"

    set_httpclient_debuglevel()

    # caplog.set_level(logging.DEBUG)

    patch_httpclient_print()

    with freezegun.freeze_time("2023-01-01"):
        _ = http.request("GET", url, timeout=3)
    # 2023-03-04 11:24:17,109 - urllib3.connectionpool - DEBUG   - Starting new HTTP connection (1): example.com:80
    # 2023-03-04 11:24:17,225 - http.client - DEBUG   - send: b'GET / HTTP/1.1\r\nHost: example.com\r\n
    #     Accept-Encoding: identity\r\nUser-Agent: python-urllib3/1.26.14\r\n\r\n'
    # 2023-03-04 11:24:17,335 - http.client - DEBUG   - reply: 'HTTP/1.1 200 OK\r\n'
    # 2023-03-04 11:24:17,337 - http.client - DEBUG   - header: Accept-Ranges: bytes
    # 2023-03-04 11:24:17,338 - http.client - DEBUG   - header: Age: 167713
    # 2023-03-04 11:24:17,338 - http.client - DEBUG   - header: Cache-Control: max-age=604800
    # 2023-03-04 11:24:17,339 - http.client - DEBUG   - header: Content-Type: text/html; charset=UTF-8
    # 2023-03-04 11:24:17,340 - http.client - DEBUG   - header: Date: Sat, 04 Mar 2023 10:24:20 GMT
    # 2023-03-04 11:24:17,340 - http.client - DEBUG   - header: Etag: "3147526947"
    # 2023-03-04 11:24:17,340 - http.client - DEBUG   - header: Expires: Sat, 11 Mar 2023 10:24:20 GMT
    # 2023-03-04 11:24:17,341 - http.client - DEBUG   - header: Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
    # 2023-03-04 11:24:17,341 - http.client - DEBUG   - header: Server: ECS (dcb/7FA3)
    # 2023-03-04 11:24:17,342 - http.client - DEBUG   - header: Vary: Accept-Encoding
    # 2023-03-04 11:24:17,342 - http.client - DEBUG   - header: X-Cache: HIT
    # 2023-03-04 11:24:17,342 - http.client - DEBUG   - header: Content-Length: 1256
    # 2023-03-04 11:24:17,343 - urllib3.connectionpool - DEBUG   - http://example.com:80 "GET / HTTP/1.1" 200 1256

    # expected = [
    #     "Starting new HTTP connection (1): example.com:80",
    #     "send: b'GET / HTTP/1.1\\r\\nHost: example.com\\r\\n
    #          Accept-Encoding: identity\\r\\nUser-Agent: python-urllib3/1.26.14\\r\\n\\r\\n'",
    #     "reply: 'HTTP/1.1 200 OK\\r\\n'",
    #     "header: Accept-Ranges: bytes",
    #     # "header: Age: 535549",
    #     # "header: Cache-Control: max-age=604800",
    #     "header: Content-Type: text/html; charset=UTF-8",
    #     # "header: Date: Sat, 04 Mar 2023 10:38:06 GMT",
    #     # 'header: Etag: "3147526947"',
    #     # "header: Expires: Sat, 11 Mar 2023 10:38:06 GMT",
    #     # "header: Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT",
    #     "header: Server: ECS (dcb/7EEC)",
    #     "header: Vary: Accept-Encoding",
    #     "header: X-Cache: HIT",
    #     "header: Content-Length: 1256",
    #     'http://example.com:80 "GET / HTTP/1.1" 200 1256',
    # ]

    # assert caplog.messages == expected
