import requests


class Api:
    """class to work with Dadata API"""

    def __init__(self, token):
        self.headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Token {token}",
        }

    def query(self, url, address, lang):
        params = {
            'query': address,
            'language': lang
        }
        data = requests.get(url=url, params=params, headers=self.headers)
        return data.json()
