import allure
from jsonschema.validators import validate

from petstore_api_project.api.delete_pet import delete_pet_200_ok, delete_pet_404_not_found
from petstore_api_project.schemas import delete_pet_schemas


@allure.tag('api')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Удаление питомца из магазин')
class TestDeletePet:

    @allure.title('Успешное удаление питомца - "200 OK"')
    def test_delete_pet_200(self, api_url, headers):
        with allure.step('Отправка запроса на удаление питомца'):
            response, id_pet = delete_pet_200_ok(api_url, headers)

        with allure.step('Проверка, что возвращается статус код 200'):
            assert response.status_code == 200
        with allure.step('Проверка, что атрибут "message" содержит id удаленного питомца'):
            assert response.json()['message'] == id_pet
        with allure.step('Проверка схемы для валидации API запросов'):
            validate(response.json(), delete_pet_schemas)


    @allure.title('Удаление несуществующего питомца - "404 Not Found')
    def test_delete_pet_404(self, api_url, headers):
        with allure.step('Отправка запроса на удаление питомца'):
            response = delete_pet_404_not_found(api_url, headers)

        with allure.step('Проверка, что возвращается статус код 404'):
            assert response.status_code == 404
