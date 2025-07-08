import allure
import pytest
from jsonschema.validators import validate

from petstore_api_project.api.find_pet import find
from petstore_api_project.schemas import get_pet_schemas


@allure.tag('api')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Поиск питомца в магазине')
class TestSearchPet:

    @pytest.mark.parametrize('pet_name', ['Spike'])
    @allure.title('Успешный поиск питомца по id')
    def test_search_pet_by_id_success(self, api_url, headers, pet_name):
        # WHEN
        with allure.step('Отправка запроса на поиcк питомца'):
            response, id_pet = find.find_pet_by_id(api_url, headers, pet_name)

        # THEN
        with allure.step('Проверка, что возвращается статус код 200'):
            assert response.status_code == 200
        with allure.step('Проверка, что атрибут "id" содержит id питомца'):
            assert response.json()['id'] == id_pet
        with allure.step('Проверка схемы для валидации API запросов'):
            validate(response.json(), get_pet_schemas)


    @pytest.mark.parametrize('id_pet', ['1111111'])
    @allure.title('Поиск питомца по несуществующему id')
    def test_search_pet_by_non_existen_id(self, api_url, id_pet):
        # WHEN
        with allure.step('Отправка запроса на поиск питомца'):
            response = find.find_pet_by_non_existen_id(api_url, id_pet)

        # THEN
        with allure.step('Проверка, что возвращается статус код 404'):
            assert response.status_code == 404
        with allure.step('Проверка, что атрибут "message" содержит id питомца'):
            assert response.json()['message'] == "Pet not found"


    @pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
    @allure.title('Успешный поиск питомца по статусу')
    def test_search_pet_by_status_success(self, api_url, status):
        # WHEN
        with allure.step('Отправка запроса на поиcк питомца'):
            response = find.find_pet_by_status(api_url, status)

        # THEN
        with allure.step('Проверка, что возвращается статус код 200'):
            assert response.status_code == 200
        with allure.step(f'Проверка, что статус первого питомца "{status}"'):
            assert response.json()[0]['status'] == status
