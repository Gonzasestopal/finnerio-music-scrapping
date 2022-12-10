from urllib.parse import urlencode, urlparse, urlunparse

def build_url(base_url, path, params=None):
    if not params:
        params = {}

    url_parts = list(urlparse(base_url))
    url_parts[2] = path
    url_parts[4] = urlencode(params)

    return urlunparse(url_parts)
