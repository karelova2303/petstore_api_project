import json

from petstore_api_project.api.api_requests import base_api


class AddPet:
    def __init__(self):
        self.endpoint = '/v2/pet'

    def add_pet(self, api_url, headers, pet_name):
        payload = json.dumps({
            "name": pet_name
        })
        response = base_api('POST', api_url=api_url, endpoint=self.endpoint, headers=headers, data=payload)
        return response

    def pet_add_unsuccess(self, api_url, headers, pet_name):
        payload = json.dumps({
            "name": pet_name
        })
        response = base_api("GET", api_url=api_url, endpoint=self.endpoint, headers=headers, data=payload)
        return response


add = AddPet()
