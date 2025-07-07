from petstore_api_project.api.add_pet import add_pet
from petstore_api_project.api.api_endpoints import ENDPOINT
from petstore_api_project.api.api_requests import  base_api


def search_pet_by_id(api_url, headers, pet_name):
    new_pet = add_pet(api_url, headers, pet_name)
    id_pet = new_pet.json()['id']

    response = base_api("GET", api_url=api_url, endpoint=f'{ENDPOINT}/{id_pet}')
    return response, id_pet


def search_pet_by_non_existen_id(api_url, id_pet):
    response = base_api("GET", api_url=api_url, endpoint=f'{ENDPOINT}/{id_pet}')
    return response


def search_pet_by_status(api_url, status):
    params = {
        'status': status
    }

    response = base_api("GET", api_url=api_url, endpoint=f'{ENDPOINT}/findByStatus', params=params)
    return response