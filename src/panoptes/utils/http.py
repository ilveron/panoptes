import requests

from panoptes.utils import logging
log = logging.get(__name__)

from typeguard import typechecked

@typechecked
class BaseHTTPClient:
    """Shared functionality for all ingestion clients (retries, headers)."""

    def __init__(self, timeout: int = 10):
        self._sess = requests.Session()
        self._sess.headers.update({"User-Agent": "OSINT-App/0.1"})
        self._timeout = timeout

    # ---- internal helpers ------------------------------------------------ #

    def _get(self, url: str, **kw):
        kw.setdefault("timeout", self._timeout)
        resp = self._sess.get(url, **kw)
        resp.raise_for_status()
        return resp


    def _post(self, url: str, **kw):
        kw.setdefault("timeout", self._timeout)
        resp = self._sess.post(url, **kw)
        resp.raise_for_status()
        return resp