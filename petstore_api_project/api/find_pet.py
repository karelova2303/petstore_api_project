from petstore_api_project.api.add_pet import add_pet_200_ok
from petstore_api_project.api.api_endpoints import ENDPOINT
from petstore_api_project.api.api_requests import  base_api


def find_pet_by_id_200_ok(api_url, headers):
    new_pet = add_pet_200_ok(api_url, headers, 'Spike')
    id_pet = new_pet.json()['id']

    response = base_api("GET", api_url=api_url, endpoint=f'{ENDPOINT}/{id_pet}')
    return response, id_pet


def find_pet_by_id_404_not_found(api_url):
    id_pet = '1111111'

    response = base_api("GET", api_url=api_url, endpoint=f'{ENDPOINT}/{id_pet}')
    return response

def find_pet_by_status_200_ok(api_url, status):
    params = {
        'status': status
    }

    response = base_api("GET", api_url=api_url, endpoint=f'{ENDPOINT}/findByStatus', params=params)
    return response