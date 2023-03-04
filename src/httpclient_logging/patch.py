"""httpclient_logging.patch."""
import http.client
import logging
import os


def set_httpclient_debuglevel() -> None:
    """if http-debuglevel > 0, debug messages in the
    http.client.HTTPConnection-class will be printed to STDOUT."""

    debug_level = int(os.getenv("DEBUGLEVEL_HTTPCONNECTION", "0"))
    # http.client.HTTPConnection.set_debuglevel(debug_level)
    http.client.HTTPConnection.debuglevel = int(debug_level)


def patch_httpclient_print() -> None:
    """Patch the print-function used in http.client to use a log-call."""
    log_http_client = logging.getLogger("http.client")

    http.client.print = lambda *args: log_http_client.debug(" ".join(args))  # type: ignore  # pragma: no cover


def unpatch_httpclient_print() -> None:
    """Unpatch the print-function used in http.client to use a log-call."""
    http.client.print = print


def configure() -> None:
    set_httpclient_debuglevel()
    patch_httpclient_print()
