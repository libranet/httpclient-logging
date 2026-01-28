"""httpclient_logging._about.

Fetch metadata from the package's pyproject.toml.
The package must be properly installed in order the metadata to be available.

"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 10):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata  # ty:ignore[unresolved-import]

PACKAGE: str = __package__ or ""


try:
    msg = importlib_metadata.metadata(PACKAGE)
    pkginfo: dict[str, str | list[str]] = msg.json
except ValueError:
    # A distribution name is required. __package__ is None
    pkginfo = {}
except importlib_metadata.PackageNotFoundError:  # pragma: no cover
    # fallback if this package is not properly installed
    pkginfo = {}


authors: str | list[str] = pkginfo.get("author_email", "unknown")

license_: str | list[str] = pkginfo.get("license_expression") or pkginfo.get("license", "unknown") or "unknown"

version: str | list[str] = pkginfo.get("version", "unknown")
