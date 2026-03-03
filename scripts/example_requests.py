#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "httpclient-logging",
#   "requests",
#   "rich",
# ]
# ///

"""Demo requests usage."""

import logging

import requests
import rich
import rich.logging

# configure colorized logging to console
# enables output from all loggers including http.client
logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s - %(message)s",
    handlers=[rich.logging.RichHandler(rich_tracebacks=False)],
)

# experiment with different levels
# logging.getLogger("example").setLevel(logging.INFO)
# logging.getLogger("http.client").setLevel(logging.INFO)
# logging.getLogger("urllib3").setLevel(logging.INFO)

log = logging.getLogger("example")

url = "https://peps.python.org/api/peps.json"

log.info(f"Fetching data from {url}")
resp = requests.get(url, timeout=5)
log.info("Requests response status code: %s", resp.status_code)
data = resp.json()

rich.print([(k, v["title"]) for k, v in data.items()][:10])
