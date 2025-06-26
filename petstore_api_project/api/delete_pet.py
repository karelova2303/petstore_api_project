from petstore_api_project.api.add_pet import add_pet_200_ok
from petstore_api_project.api.api_endpoints import ENDPOINT
from petstore_api_project.api.api_requests import base_api



def delete_pet_200_ok(api_url, headers):
    new_pet = add_pet_200_ok(api_url, headers, 'Monkey')
    id_pet = str(new_pet.json()['id'])

    response = base_api("DELETE", api_url=api_url, endpoint=f'{ENDPOINT}/{id_pet}')
    return response, id_pet


def delete_pet_404_not_found(api_url, headers):
    new_pet = add_pet_200_ok(api_url, headers, 'Monkey')
    id_pet = str(new_pet.json()['id'])

    for _ in range(2):
        response = base_api("DELETE", api_url=api_url, endpoint=f'{ENDPOINT}/{id_pet}')

    return response
