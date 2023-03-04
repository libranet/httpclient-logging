# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module httpclient_logging.patch."""
import http.client
import logging
import os
import urllib3


def test_httpclient_debuglevel():
    from httpclient_logging.patch import set_http_debuglevel

    # implicit default
    assert http.client.HTTPConnection.debuglevel == 0

    # explicit default
    os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "0"
    set_http_debuglevel()
    assert http.client.HTTPConnection.debuglevel == 0

    os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "1"
    set_http_debuglevel()
    assert http.client.HTTPConnection.debuglevel == 1


def test_configure():
    from httpclient_logging import configure

    configure()


def test_unpatched_httpclient_print(capsys):
    from httpclient_logging.patch import set_http_debuglevel, patch_httpclient_print, unpatch_httpclient_print

    os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "1"
    set_http_debuglevel()

    assert http.client.HTTPConnection.debuglevel == 1

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

    unpatch_httpclient_print()
    pm = urllib3.PoolManager()
    url = "http://webcode.me"
    # breakpoint()
    resp = pm.request("GET", url)
    # captured = capsys.readouterr()
    # assert "http.client - DEBUG   - reply:" in  captured.err
    # assert captured.out == ""

    # header: Server: nginx/1.6.2
    # header: Date: Sat, 04 Mar 2023 01:21:17 GMT
    # header: Content-Type: text/html
    # header: Content-Length: 394
    # header: Last-Modified: Sun, 23 Jan 2022 10:39:25 GMT
    # header: Connection: keep-alive
    # header: ETag: "61ed305d-18a"
    # header: Access-Control-Allow-Origin: *
    # header: Accept-Ranges: bytes

    patch_httpclient_print()
    pm = urllib3.PoolManager()
    url = "http://webcode.me"
    resp = pm.request("GET", url)
    # captured = capsys.readouterr()
    # assert "http.client - DEBUG   - reply:" in  captured.err
    # assert captured.out == ""

    # 2023-03-04 02:22:02,527 - urllib3.connectionpool - DEBUG   - Starting new HTTP connection (1): webcode.me:80
    # 2023-03-04 02:22:02,624 - urllib3.connectionpool - DEBUG   - http://webcode.me:80 "GET / HTTP/1.1" 200 394
    # 2023-03-04 02:22:02,625 - urllib3.connectionpool - DEBUG   - Starting new HTTP connection (1): webcode.me:80
    # 2023-03-04 02:22:02,685 - http.client - DEBUG   - send: b'GET / HTTP/1.1\r\nHost: webcode.me\r\nAccept-Encoding: identity\r\nUser-Agent: python-urllib3/1.26.14\r\n\r\n'
    # 2023-03-04 02:22:02,725 - http.client - DEBUG   - reply: 'HTTP/1.1 200 OK\r\n'
    # 2023-03-04 02:22:02,726 - http.client - DEBUG   - header: Server: nginx/1.6.2
    # 2023-03-04 02:22:02,726 - http.client - DEBUG   - header: Date: Sat, 04 Mar 2023 01:21:17 GMT
    # 2023-03-04 02:22:02,726 - http.client - DEBUG   - header: Content-Type: text/html
    # 2023-03-04 02:22:02,727 - http.client - DEBUG   - header: Content-Length: 394
    # 2023-03-04 02:22:02,727 - http.client - DEBUG   - header: Last-Modified: Sun, 23 Jan 2022 10:39:25 GMT
    # 2023-03-04 02:22:02,727 - http.client - DEBUG   - header: Connection: keep-alive
    # 2023-03-04 02:22:02,727 - http.client - DEBUG   - header: ETag: "61ed305d-18a"
    # 2023-03-04 02:22:02,727 - http.client - DEBUG   - header: Access-Control-Allow-Origin: *
    # 2023-03-04 02:22:02,727 - http.client - DEBUG   - header: Accept-Ranges: bytes
    # 2023-03-04 02:22:02,727 - urllib3.connectionpool - DEBUG   - http://webcode.me:80 "GET / HTTP/1.1" 200 394

    # resp = pm.request('GET', url)
    # captured = capsys.readouterr()
    # assert captured.err == ""
    # assert captured.out == ""

    # import requests

    # url = "https://reqbin.com/echo/get/json"

    # resp = requests.get(url,  headers={'Accept': 'application/json'})


# def test_monkeypatch_httpclient_print():
#     from httpclient_logging.patch import set_http_debuglevel, monkeypatch_httpclient_print

#     os.environ["DEBUGLEVEL_HTTPCONNECTION"] = "1"
#     set_http_debuglevel()
#     monkeypatch_httpclient_print()
