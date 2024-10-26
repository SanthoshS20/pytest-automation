import requests, logging
from typing import Optional, Dict

# Type Hinting
def make_api_call(url: str, query_params: Dict[str, str], request_body: Optional[Dict[str, str]] = None,
                  method: Optional[str] = 'GET', request_headers: Optional[Dict[str, str]] = None,
                  auth: Optional[Dict[str, str]] = None, timeout: Optional[int] = None):
    """
    makes an API call with the help of requests python library.

    Parameters:
        url (str): url of the API
        query_params (dict): query params of the API
        request_body (dict): request body of the API (optional)
        method (dict): HTTP method (optional)
        request_headers (dict): Request headers of the API (optional)
        auth (dict): Authentication data for the API (optional)
        timeout (int): Timeout for an API

    Returns:
        API_response (dict): API response for a request

    Raises:
        HTTPError: If the response code other than 200 and 201
    """
    try:
        response = requests.request(method, url, params=query_params, data=request_body, headers=request_headers,
                                    auth=auth, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.HTTPError as http_error:
        raise requests.HTTPError("Incorrect response code")
        #logging.error(f"Request failed with the http error : {http_error}")
