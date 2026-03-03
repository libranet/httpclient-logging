#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "httpclient-logging",
#   "libranet-logging",
#   "requests",
#   "rich",
# ]
# ///

"""Demo requests usage."""

import json
import logging
import urllib.request

# configure colorized logging to console
# enables output from all loggers including http.client
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(name)s - %(message)s",
#     handlers=[rich.logging.RichHandler(rich_tracebacks=False)],
# )
import libranet_logging
import rich
import rich.logging

libranet_logging.initialize()

# experiment with different levels
# logging.getLogger("example").setLevel(logging.INFO)
# logging.getLogger("http.client").setLevel(logging.INFO)
# logging.getLogger("urllib3").setLevel(logging.INFO)

log = logging.getLogger("example")

url = "https://peps.python.org/api/peps.json"

log.info(f"Fetching data from {url}")
resp = urllib.request.urlopen(url, timeout=5)
log.info("Requests response status code: %s", resp.code)
data = json.load(resp)

rich.print([(k, v["title"]) for k, v in data.items()][:10])
