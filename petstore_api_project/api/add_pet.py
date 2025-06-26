import json

from petstore_api_project.api.api_endpoints import ENDPOINT
from petstore_api_project.api.api_requests import base_api


def add_pet_200_ok(api_url, headers, pet_name):
    payload = json.dumps({
        "name": pet_name
    })
    response = base_api('POST', api_url=api_url, endpoint=ENDPOINT, headers=headers, data=payload)
    return response


def add_pet_405_method_not_allowed(api_url, headers, pet_name):
    payload = json.dumps({
        "name": pet_name
    })
    response = base_api("GET", api_url=api_url, endpoint=ENDPOINT, headers=headers, data=payload)
    return response
