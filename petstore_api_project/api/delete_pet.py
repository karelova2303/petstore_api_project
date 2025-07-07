from petstore_api_project.api.add_pet import add_pet
from petstore_api_project.api.api_endpoints import ENDPOINT
from petstore_api_project.api.api_requests import base_api



def delete_pet(api_url, headers, pet_name):
    new_pet = add_pet(api_url, headers, pet_name)
    id_pet = str(new_pet.json()['id'])

    response = base_api("DELETE", api_url=api_url, endpoint=f'{ENDPOINT}/{id_pet}')
    return response, id_pet


def delete_pet_unsuccess(api_url, id_pet):
    response = base_api("DELETE", api_url=api_url, endpoint=f'{ENDPOINT}/{id_pet}')

    return response
