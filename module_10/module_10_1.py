from time import sleep
from time import time

def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово №{i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_time = time()
print(f'Работа потоков {end_time - start_time}')