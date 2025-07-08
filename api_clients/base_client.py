import requests as re

class BaseClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session = re.Session()

    def _build_url(self, endpoint):
        return self.base_url+endpoint

    def _request(self, method, endpoint, **kwargs):
        url = self._build_url(endpoint)
        resp = self.session.request(
            url=url,
            method=method, 
            **kwargs
        )
        return resp

    def _get(self, endpoint, params = None, **kwargs):
        return self._request('GET', endpoint, params = params, **kwargs)
    
    def _post(self, endpoint, json=None, data=None, **kwargs):
        return self._request('POST', endpoint, json=json, data=data, **kwargs)

    def _put(self, endpoint, json=None, data=None, **kwargs):
        return self._request('PUT', endpoint, json=json, data=data, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self._request('DELETE', endpoint, **kwargs)

    def close(self):
        self.session.close()