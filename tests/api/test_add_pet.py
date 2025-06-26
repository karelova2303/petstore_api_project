import allure
from jsonschema.validators import validate

from petstore_api_project.api.add_pet import add_pet_200_ok, add_pet_405_method_not_allowed
from petstore_api_project.schemas import post_pet_schemas

pet_name = 'Dandy'


@allure.tag('api')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Добавление питомца в магазин')
class TestAddPet:

    @allure.title('Успешное добавление - "200 OK"')
    def test_add_pet_200(self, api_url, headers):
        with allure.step('Отправка запроса на добавление питомца'):
            response = add_pet_200_ok(api_url, headers, pet_name)

        with allure.step('Проверка, что возвращается статус код 200'):
            assert response.status_code == 200
        with allure.step(f'Проверка, что имя питомца - "{pet_name}"'):
            assert response.json()['name'] == pet_name
        with allure.step('Проверка схемы для валидации API запросов'):
            validate(response.json(), post_pet_schemas)

    @allure.title('Неуспешное добавление - "405 Method Not Allowed"')
    def test_add_pet_405(self, headers, api_url):
        with allure.step('Отправка запроса на добавление питомца'):
            response = add_pet_405_method_not_allowed(api_url, headers, pet_name)

        with allure.step('Проверка, что возвращается статус код 405'):
            assert response.status_code == 405
