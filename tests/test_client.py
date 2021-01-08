from vps_backend_assessment.swapi.client import SWAPIClient
from vps_backend_assessment.swapi.models import Starship

from nose.tools import assert_equals

import os, sys
import httpretty

BASE_URL = 'https://swapi.dev/api/starships/'

@httpretty.activate
def test_fetch_starships():
    """
        Tests that the SWAPIClient can fetch starships from the API
    """
    # Open and fetch the sample json request
    f = open('tests/data/sample_request.json', 'r')
    sample_json = f.read()

    # Register the BASE_URL with httpretty
    httpretty.register_uri(
        httpretty.GET,
        BASE_URL,
        body=sample_json
    )
    
    # Initialize the client and fetch the starship collection
    swapi_client = SWAPIClient()
    starship_collection = swapi_client.fetch_starships()

    # Assert that we have the expected number of elements
    assert_equals(starship_collection.length(), 10)

    # Assert that we have Starship objects in the collection
    for starship in starship_collection.iter():
        assert_equals(type(starship), Starship)
    
    