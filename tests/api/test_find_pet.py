import allure
import pytest
from jsonschema.validators import validate

from petstore_api_project.api.find_pet import find_pet_by_id_404_not_found, find_pet_by_id_200_ok, \
    find_pet_by_status_200_ok
from petstore_api_project.schemas import get_pet_schemas


@allure.tag('api')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Поиск питомца в магазине')
class TestFindPet:

    @allure.title('Успешный поиск питомца по id - "200 OK"')
    def test_find_pet_by_id_200(self, api_url, headers):
        with allure.step('Отправка запроса на поиcк питомца'):
            response, id_pet = find_pet_by_id_200_ok(api_url, headers)

        with allure.step('Проверка, что возвращается статус код 200'):
            assert response.status_code == 200
        with allure.step('Проверка, что атрибут "id" содержит id питомца'):
            assert response.json()['id'] == id_pet
        with allure.step('Проверка схемы для валидации API запросов'):
            validate(response.json(), get_pet_schemas)


    @allure.title('Поиск питомца по несуществующему id - "404 Not Found')
    def test_find_pet_by_id_404(self, api_url):
        with allure.step('Отправка запроса на поиск питомца'):
            response = find_pet_by_id_404_not_found(api_url)

        with allure.step('Проверка, что возвращается статус код 404'):
            assert response.status_code == 404
        with allure.step('Проверка, что атрибут "message" содержит id питомца'):
            assert response.json()['message'] == "Pet not found"



    @pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
    @allure.title('Успешный поиск питомца по статусу - "200 OK"')
    def test_find_pet_by_status_pending_200(self, api_url, status):
        with allure.step('Отправка запроса на поиcк питомца'):
            response = find_pet_by_status_200_ok(api_url, status)

        with allure.step('Проверка, что возвращается статус код 200'):
            assert response.status_code == 200
        with allure.step(f'Проверка, что статус первого питомца "{status}"'):
            assert response.json()[0]['status'] == status
