"""httpclient_logging.patch."""

from __future__ import annotations

import http.client
import logging
import os
import typing

# ``http.client`` emits its debug output through the module-global name ``print``.
# Both ``patch_httpclient_print`` and ``unpatch_httpclient_print`` rebind that name
# at runtime (a monkeypatch). The typed ``http.client`` module exposes no ``print``
# attribute, so route the rebinding through an ``Any`` view to keep mypy and ty quiet
# without sprinkling per-line ignores.
_http_client: typing.Any = http.client

pre_patched_value = print

log = logging.getLogger(__name__)


def set_httpclient_debuglevel(debuglevel: int | str | None = None) -> None:
    """Set debug-level for http.client.

    If http-debuglevel > 0, debug messages in the http.client.HTTPConnection-class will be printed to STDOUT.
    """
    if debuglevel is None:
        debuglevel = os.getenv("DEBUGLEVEL_HTTPCONNECTION", "0")

    try:
        debuglevel = int(debuglevel)
    except ValueError:
        log.warning(f"Cannot change http.client.HTTPConnection.debuglevel: {debuglevel} is not an integer.")
        return

    http.client.HTTPConnection.debuglevel = debuglevel
    log.debug(f"Setting http.client.HTTPConnection.debuglevel to {debuglevel}")


def patch_httpclient_print() -> None:
    """Patch the print-function used in http.client to use a call to log.debug() instead."""
    log_http_client = logging.getLogger("http.client")
    _http_client.print = lambda *args: log_http_client.debug(" ".join(args))


def unpatch_httpclient_print() -> None:
    """Unpatch the print-function used in http.client."""
    _http_client.print = pre_patched_value


def configure() -> None:
    """Configure the http.client.HTTPConnection-class.

    Configure this class to use the debuglevel from an environment-variable DEBUGLEVEL_HTTPCONNECTION
    and to use a logger instead of a print-statements to output to standard output.
    """
    set_httpclient_debuglevel(debuglevel=1)
    patch_httpclient_print()


def undo() -> None:
    """Undo the configured steps."""
    set_httpclient_debuglevel(debuglevel=0)
    unpatch_httpclient_print()
