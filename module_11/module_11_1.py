import requests
import numpy as np
import matplotlib.pyplot as plt

# GET-request ----------------------------------------
url = 'https://api.github.com' # URL для запроса

response = requests.get(url) # Отправка GET-запроса

# Проверка статуса ответа
if response.status_code == 200:
    print('Успешный GET-запрос!')
    print('Ответ:', response.json())
else:
    print('Ошибка GET-запроса:', response.status_code)

# POST-request
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

# Загрузка файла

url = 'http://таксимо-адм.рф/tinybrowser/images/session/5_soziv_4_session/1.-reshenie-19-ot-26.12.23g..doc' # URL для загрузки файла

response = requests.get(url) # Отправка GET-запроса для загрузки файла

# Проверка статуса ответа
if response.status_code == 200:
    # Сохранение файла
    with open('reshenie_19.doc', 'wb') as f: # Загружает и сохраняет реальный файл из сети
        f.write(response.content)
    print('Файл успешно загружен!')
else:
    print('Ошибка загрузки файла:', response.status_code)

# Работа с numpy -----------------------------------------------

# Создание одномерного массива
array_1d = np.array([1, 2, 3, 4, 5])
print("Одномерный массив:", array_1d)

# Выполнение математических операций
# Сложение
array_sum = array_1d + 10
print("Сложение с 10:", array_sum)

# Умножение
array_product = array_1d * 2
print("Умножение на 2:", array_product)

# Вычисление среднего значения
mean_value = np.mean(array_1d)
print("Среднее значение:", mean_value)

# Сложение двух массивов
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
array_sum = array_1 + array_2
print("Сумма двух массивов:", array_sum)

# Работа с matplotlib -----------------------------------------

# Данные для линейного графика
x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
y = np.sin(x)  # Значения функции синуса

# Создание линейного графика
plt.figure(figsize=(10, 5))  # Размер графика
plt.plot(x, y, label='sin(x)', color='blue')  # Линейный график
plt.title('Линейный график функции синуса')  # Заголовок графика
plt.xlabel('x')  # Подпись оси x
plt.ylabel('sin(x)')  # Подпись оси y
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Горизонтальная линия на уровне 0
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Вертикальная линия на уровне 0
plt.grid()  # Сетка
plt.legend()  # Легенда
plt.show()  # Показать график

# Данные для гистограммы
data = np.random.randn(1000)  # Генерация 1000 случайных чисел из нормального распределения

# Создание гистограммы
plt.figure(figsize=(10, 5))  # Размер графика
plt.hist(data, bins=30, color='orange', edgecolor='black')  # Гистограмма
plt.title('Гистограмма случайных чисел')  # Заголовок графика
plt.xlabel('Значение')  # Подпись оси x
plt.ylabel('Частота')  # Подпись оси y
plt.grid()  # Сетка
plt.show()  # Показать график