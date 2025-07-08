from petstore_api_project.api.add_pet import add
from petstore_api_project.api.api_requests import base_api


class DeletePet:
    def __init__(self):
        self.endpoint = '/v2/pet'

    def delete_pet(self, api_url, headers, pet_name):
        new_pet = add.add_pet(api_url, headers, pet_name)
        id_pet = str(new_pet.json()['id'])

        response = base_api("DELETE", api_url=api_url, endpoint=f'{self.endpoint}/{id_pet}')
        return response, id_pet

    def delete_pet_unsuccess(self, api_url, id_pet):
        response = base_api("DELETE", api_url=api_url, endpoint=f'{self.endpoint}/{id_pet}')

        return response


delete = DeletePet()
