import ujson as json
import requests

from requests import Response

class ApiError(Exception):
    """
        An exception to represent an error that occurs when trying to
        fetch from the SWAPI
    """
    pass

def fetch(url: str) -> Response:
    """
        Fetches the given URL and returns the Response object retrieved from 
        the get operation.
    """
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            raise ApiError(f'GET {url} failed: {resp.status_code}')
        return resp
    except ApiError as e:
        print(e)

