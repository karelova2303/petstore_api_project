import allure
import pytest
from jsonschema.validators import validate

from petstore_api_project.api.delete_pet import delete_pet, delete_pet_unsuccess
from petstore_api_project.schemas import delete_pet_schemas


@allure.tag('api')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Удаление питомца из магазина')
class TestDeletePet:

    @pytest.mark.parametrize('pet_name', ['Monkey'])
    @allure.title('Успешное удаление')
    def test_delete_pet_success(self, api_url, headers, pet_name):
        with allure.step('Отправка запроса на удаление питомца'):
            response, id_pet = delete_pet(api_url, headers, pet_name)

        with allure.step('Проверка, что возвращается статус код 200'):
            assert response.status_code == 200
        with allure.step('Проверка, что атрибут "message" содержит id удаленного питомца'):
            assert response.json()['message'] == id_pet
        with allure.step('Проверка схемы для валидации API запросов'):
            validate(response.json(), delete_pet_schemas)


    @pytest.mark.parametrize('id_pet', ['1111111'])
    @allure.title('Удаление несуществующего питомца')
    def test_delete_non_exist_pet(self, api_url, id_pet):
        with allure.step('Отправка запроса на удаление питомца'):
            response = delete_pet_unsuccess(api_url, id_pet)

        with allure.step('Проверка, что возвращается статус код 404'):
            assert response.status_code == 404
