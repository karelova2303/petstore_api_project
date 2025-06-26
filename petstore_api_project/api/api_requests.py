import requests

from petstore_api_project.utils.logging_helper import response_logging, response_attaching


def base_api(method, api_url, endpoint, **kwargs):
    url = f"{api_url}{endpoint}"
    response = requests.request(
        method=method,
        url=url,
        **kwargs
    )
    response_logging(response)
    response_attaching(response)
    return response

