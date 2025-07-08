from petstore_api_project.api.add_pet import add
from petstore_api_project.api.api_requests import base_api


class FindPet:
    def __init__(self):
        self.endpoint = '/v2/pet'

    def find_pet_by_id(self, api_url, headers, pet_name):
        new_pet = add.add_pet(api_url, headers, pet_name)
        id_pet = new_pet.json()['id']

        response = base_api("GET", api_url=api_url, endpoint=f'{self.endpoint}/{id_pet}')
        return response, id_pet

    def find_pet_by_non_existen_id(self, api_url, id_pet):
        response = base_api("GET", api_url=api_url, endpoint=f'{self.endpoint}/{id_pet}')
        return response

    def find_pet_by_status(self, api_url, status):
        params = {
            'status': status
        }

        response = base_api("GET", api_url=api_url, endpoint=f'{self.endpoint}/findByStatus', params=params)
        return response


find = FindPet()
