from vps_backend_assessment.swapi.utilities import fetch
from nose.tools import assert_true

import httpretty

BASE_URL='http://example.com/api'

@httpretty.activate
def test_fetch_url():
    """
        Tests that the `fetch` method can fetch a URL and return a response
    """

    # Register the URL with httpretty
    httpretty.register_uri(
        httpretty.GET,
        BASE_URL,
        body='{"origin": "127.0.0.1"}'
    )

    # Fetch the response from the URL
    response = fetch(BASE_URL)

    # Assert that the response JSON matches the expected value
    assert_true(response.json() == {'origin': '127.0.0.1'})

