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
    "lead_email": "aaa@mail.ru",
    "phone_number": "+7 952 255 44 55",
    "order_date": "31.12.2022",
    "description": "dddd fff ssss"
}
response = send_request_to_get_form(dict_name_value_pairs)
print(f'Answer of request: {json.load(response)}, status code: {response.status}')

# форма не полностью, полей в форме больше
dict_name_value_pairs = {
    "email": "aaa@mail.ru",
    "user_number": "+7 952 255 44 55",
    "date_of_birth": "31.12.2022",
    "user_name": "John"
}

response = send_request_to_get_form(dict_name_value_pairs)
print(f'Answer of request: {json.load(response)}, status code: {response.status}')

# форма не полностью, полей в форме меньше
dict_name_value_pairs = {
    "lead_email": "aaa@mail.ru",
    "phone_number": "+7 952 255 44 55",
    "order_date": "31.12.2022",
}

response = send_request_to_get_form(dict_name_value_pairs)
print(f'Answer of request: {json.load(response)}, status code: {response.status}')

# форма пуста, ошибка 400
dict_name_value_pairs = {
}
response = send_request_to_get_form(dict_name_value_pairs)
