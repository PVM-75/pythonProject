import requests

# GET-request ----------------------------------------
url = 'https://api.github.com' # URL для запроса

response = requests.get(url) # Отправка GET-запроса

# Проверка статуса ответа
if response.status_code == 200:
    print('Успешный GET-запрос!')
    print('Ответ:', response.json())
else:
    print('Ошибка GET-запроса:', response.status_code)

# POST-request ----------------------------------------------
url = 'https://httpbin.org/post' # URL для запроса

# Данные для отправки
data = {
    'name': 'John',
    'age': 30
}

response = requests.post(url, json=data) # Отправка POST-запроса

# Проверка статуса ответа
if response.status_code == 200:
    print('Успешный POST-запрос!')
    print('Ответ:', response.json())
else:
    print('Ошибка POST-request:', response.status_code)

# Загрузка файла ---------------------------------------------

url = 'http://таксимо-адм.рф/tinybrowser/images/session/5_soziv_4_session/1.-reshenie-19-ot-26.12.23g..doc' # URL для загрузки файла

response = requests.get(url) # Отправка GET-запроса для загрузки файла

# Проверка статуса ответа
if response.status_code == 200:
    # Сохранение файла
    with open('reshenie_19.doc', 'wb') as f:
        f.write(response.content)
    print('Файл успешно загружен!')
else:
    print('Ошибка загрузки файла:', response.status_code)

