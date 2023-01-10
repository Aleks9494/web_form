import json
import urllib.request
import urllib.parse


def send_request_to_get_form(values):
    json_bytes = json.dumps(values).encode('utf-8')
    url = f"http://localhost:8010/api/v1/get_form"
    request = urllib.request.Request(url, json_bytes, method='POST')
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    try:
        response = urllib.request.urlopen(request)
    except Exception as e:
        print(f"Request not completed, the reason is {str(e)}")
    else:
        return response


url = "http://localhost:8010/api/v1/create_collection/"
request = urllib.request.Request(url)
request.add_header('Content-Type', 'application/json; charset=utf-8')

try:
    response = urllib.request.urlopen(request)
except Exception as e:
    print(f"Request not completed, the reason is {str(e)}")
else:
    print(json.load(response))

# форма полностью
dict_name_value_pairs = {
    "name": "Form 2",
    "lead_email": "bbb@mail.ru",
    "phone_number": "+7 952 259 99 45",
    "order_date": "2022-11-30",
    "description": "Описание формы 2"
}
response = send_request_to_get_form(dict_name_value_pairs)
print(f'Answer of request: {json.load(response)}, status code: {response.status}')

# форма не полностью, поля совпадают с шаблоном
dict_name_value_pairs = {
    "lead_email": "eee@mail.ru",
    "phone_number": "+7 952 259 99 48",
    "description": "Описание формы 5"
}

response = send_request_to_get_form(dict_name_value_pairs)
print(f'Answer of request: {json.load(response)}, status code: {response.status}')

# форма не полностью, полей в форме больше
dict_name_value_pairs = {
    "name": "Form 5",
    "lead_email": "eee@mail.ru",
    "phone_number": "+7 952 259 99 48",
    "description": "Описание формы 5"
}

response = send_request_to_get_form(dict_name_value_pairs)
print(f'Answer of request: {json.load(response)}, status code: {response.status}')

# форма не полностью, полей в форме меньше
dict_name_value_pairs = {
    "name": "Form 2",
    "lead_email": "bbb@mail.ru",
    "order_date": "2022-11-30",
    "description": "Описание формы 2"
}

response = send_request_to_get_form(dict_name_value_pairs)
print(f'Answer of request: {json.load(response)}, status code: {response.status}')

# форма пуста, ошибка 400
dict_name_value_pairs = {
}
response = send_request_to_get_form(dict_name_value_pairs)

# ошибка валидации мейла
dict_name_value_pairs = {
    "name": "Form 2",
    "lead_email": "bbbmail.ru",
    "order_date": "2022-11-30",
    "description": "Описание формы 2"
}
send_request_to_get_form(dict_name_value_pairs)

# ошибка валидации даты
dict_name_value_pairs = {
    "name": "Form 2",
    "lead_email": "bbb@mail.ru",
    "order_date": "2022-11-33",
    "description": "Описание формы 2"
}
send_request_to_get_form(dict_name_value_pairs)

# ошибка валидации даты еше раз
dict_name_value_pairs = {
    "name": "Form 2",
    "lead_email": "bbb@mail.ru",
    "order_date": "33.11.2022",
    "description": "Описание формы 2"
}
send_request_to_get_form(dict_name_value_pairs)

# ошибка валидации телефона
dict_name_value_pairs = {
    "lead_email": "eee@mail.ru",
    "phone_number": "+7 952 259 9948",
    "description": "Описание формы 5"
}
send_request_to_get_form(dict_name_value_pairs)
