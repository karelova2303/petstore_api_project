import allure
import pytest
from jsonschema.validators import validate

from petstore_api_project.api.add_pet import add_pet, pet_add_unsuccess
from petstore_api_project.schemas import post_pet_schemas


@allure.tag('api')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Добавление питомца в магазин')
class TestAddPet:

    @pytest.mark.parametrize('pet_name', ['Dandy'])
    @allure.title('Успешное добавление')
    def test_add_pet_success(self, api_url, headers, pet_name):
        with allure.step('Отправка запроса на добавление питомца'):
            response = add_pet(api_url, headers, pet_name)

        with allure.step('Проверка, что возвращается статус код 200'):
            assert response.status_code == 200
        with allure.step(f'Проверка, что имя питомца - "{pet_name}"'):
            assert response.json()['name'] == pet_name
        with allure.step('Проверка схемы для валидации API запросов'):
            validate(response.json(), post_pet_schemas)


    @pytest.mark.parametrize('pet_name', ['Dandy'])
    @allure.title('Неуспешное добавление')
    def test_add_pet_unsuccess(self, headers, api_url, pet_name):
        with allure.step('Отправка запроса на добавление питомца'):
            response = pet_add_unsuccess(api_url, headers, pet_name)

        with allure.step('Проверка, что возвращается статус код 405'):
            assert response.status_code == 405
