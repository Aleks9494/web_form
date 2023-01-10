Для запуска проекта
создать папку logs в корне проекта
sudo docker-compose build
sudo docker-compose up

Для проверки
1)  Воспользоваться встроенным OpenApi (Swagger) для FastApi.
    Выполнить GET запрос к роуту '/api/v1/create_collection' для создания коллекции в MongoDB.
    Выполнить POST запрос к роуту '/api/v1/get_form' c необходимыми данными в теле запроса в виде JSON.

2)  Воспользоваться скриптом test_script.py. Запуск командой python3 test_script.py из папки с проектом.
    Контейнеры с приложением и БД должны быть запущены.
    Скрипт использует стандартную библиотеку запросов urllib, устанавливать ничего не нужно.
    Ответы на запросы к серверу:
        "Имя формы" - форма найдена
        {"name_field": "type_field", "name_field": "type_field", ... } - форма не найдена
        Ошибка 400 - пустая форма в теле запроса

Данные (data) для сохранения в БД можно поменять в модуле utils.py
Затем либо выполнить запрос для создания коллекции, либо еще раз запустить скрипт

Данные для проверки с помощью скрипта можно изменить в скрипте