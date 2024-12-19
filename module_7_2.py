import io

def custom_write(file_name, strings):
    strings_positions = {}
    string = 0
    byte = 0
    for item in strings:
        string += 1
        file = open(file_name, 'a', encoding='utf-8') # Работаем с файлом
        byte = file.tell() # Если открыть файл в режиме append, курсор становится в конце файла!
        file.write(f'{item}\n')
        file.close()
        strings_positions[(string, byte)] = item # Работаем с выводом из функции
    return strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)