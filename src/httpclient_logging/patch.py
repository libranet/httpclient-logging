"""httpclient_logging.patch."""
import http.client
import logging
import os


pre_patched_value = print

log = logging.getLogger(__name__)


def set_httpclient_debuglevel(debug_level=None) -> None:
    """if http-debuglevel > 0, debug messages in the
    http.client.HTTPConnection-class will be printed to STDOUT."""

    if not debug_level:
        debug_level = os.getenv("DEBUGLEVEL_HTTPCONNECTION", "0")

    try:
        debug_level = int(debug_level)
    except ValueError:
        log.warning(f"Cannot change http.client.HTTPConnection.debuglevel: {debug_level} is not an integer.")
        return

    http.client.HTTPConnection.debuglevel = debug_level
    log.debug(f"Setting http.client.HTTPConnection.debuglevel to {debug_level}")


def patch_httpclient_print() -> None:
    """Patch the print-function used in http.client to use a call to log.debug() instead."""
    log_http_client = logging.getLogger("http.client")
    http.client.print = lambda *args: log_http_client.debug(" ".join(args))  # type: ignore  # pragma: no cover


def unpatch_httpclient_print() -> None:
    """Unpatch the print-function used in http.client."""
    http.client.print = pre_patched_value  # type: ignore


def configure() -> None:
    """Configure the http.client.HTTPConnection-class

    Configure this class to use the debuglevel from an environment-variable DEBUGLEVEL_HTTPCONNECTION
    and to use a logger instead of a print-statements to output to standard output.
    """
    set_httpclient_debuglevel(debug_level=1)
    patch_httpclient_print()


def undo() -> None:
    """Undo the configured steps.
    """
    set_httpclient_debuglevel(debug_level=0)
    unpatch_httpclient_print()


def cancel():
    "Dummy function to cancel (override) the entrypoint-registration."
    pass
