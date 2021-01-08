import requests
import ujson as json

from .utilities import fetch

from .models import (
    Starship,
    StarshipCollection
)

class ApiError(BaseException):
    pass

class SWAPIClient(object):
    """
        API Client to the SWAPI
    """
    BASE_URL = "https://swapi.dev/api"

    def __init__(self):
        pass

    def fetch_starships(self) -> StarshipCollection:
        """
            Fetches all starships from the SWAPI, paginating through all the results, and returns a StarshipCollection
        """
        urls_to_query = []
        starships = []

        urls_to_query.append(f'{self.BASE_URL}/starships/')

        while (len(urls_to_query) > 0):
            url = urls_to_query.pop()
            
            # Fetch the content from the URL
            resp = fetch(url)

            json_data = json.loads(resp.content)

            # While there is a next page, append to the list of URLs to query
            if json_data['next'] != None:
                urls_to_query.append(json_data['next'])

            # Construct a Starship object and append it to our list
            for item in json_data['results']:
                starship = Starship(**item)
                starships.append(starship)
        return StarshipCollection(starships)