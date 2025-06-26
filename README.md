<h1> Проект по тестированию API "Petstore"</h1>

<a target="_blank" href="https://petstore.swagger.io/">***Ссылка на "Petstore"***</a>

![This is an image](/resources/images/petstore_logo.png)

<h3> Список проверок, реализованных в автотестах:</h3>

### API-тесты
- [x] Проверка добавления питомца в магазин
  - Успешное / неуспешное добавление
- [x] Поиск питомца в магазине
  - Успешный / неуспешный поиск по id
  - Поиск по статусу
- [x] Удаление питомца из магазина
  - Успешное / неуспешное удаление

----
### Проект реализован с использованием:
<div align="center">
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/python-original-wordmark.svg" 
    title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/pytest-original-wordmark.svg" 
    title="Pytest" alt="Pytest" width="45" height="45"/>&nbsp; 
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selenium-original1.svg" 
    title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;  
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selene.png" 
    title="Selene" alt="Selene" width="50" height="50"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/requests.png" 
    title="Requests" alt="Requests" width="40" height="40"/>&nbsp;  
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/pycharm-original.svg" 
    title="PyCharm" alt="PyCharm" width="40" height="40"/>&nbsp;    
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/jenkins-original.svg" 
    title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/Allure.svg" 
    title="Allure Report" alt="Allure Report" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/AllureTestOps.png" 
    title="Allure TestOps" alt="Allure TestOps" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/telegram1.png" 
    title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp;
<img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/Jira.png" 
    title="Telegram" alt="Jira" width="40" height="40"/>&nbsp;
</div>

----
### Локальный запуск

1. Склонировать репозиторий
2. Установить зависимости командой `pip install -r requirements.txt`
3. Открыть проект в PyCharm, установить интерпретатор
4. Запустить тесты в командной строке: `pytest`  


----
### Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/019-karelova2303-petstore_api_project/">_**Ссылка на сборку в Jenkins**_</a>


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/019-karelova2303-petstore_api_project/">проект</a>
2. Выбрать пункт `Build Now`

![jenkins job main page](/resources/images/Jenkins_job_main_page.png)


----
### Allure отчет

#### Формирование отчета:
>-  локальный запуск: ввести в командной строке `allure serve allure-results`
>-  запуск через Jenkins: кликнуть кнопку `Allure Report` в боковом меню 


#### Результаты запусков
![This is an image](/resources/images/allure_report_overview.png)
![This is an image](resources/images/allure_report_graphs.png)
![This is an image](resources/images/allure_report_test.png)



----
### Интеграция с Allure TestOps

> <a target="_blank" href="https://allure.autotests.cloud/project/4814/dashboards">_**Ссылка на проект в Allure TestOps**_</a>

#### Пример dashboard с общими результатами тестирования
![This is an image](/resources/images/allure_TestOps_test_dashboard_all.png)

#### Общий список всех тест-кейсов
![This is an image](/resources/images/allure_TestOps_test_cases.png)

#### Пример отчёта выполнения одного из автотестов
![This is an image](/resources/images/example_autotests_allure_TestOps.png)

#### Пример dashboard с результатами запуска
![This is an image](/resources/images/allure_TestOps_dashboard_ex.png)

#### История запуска тестовых наборов
![This is an image](/resources/images/allure_TestOps_launches.png)

----
### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1468">_**Ссылка на задачу в Jira**_</a>

![This is an image](/resources/images/jira.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](/resources/images/tg_notification.png)

