from pprint import pprint
import builtins

def introspection_info(obj):
    obj_type = type(obj) # Получаем тип объекта
    attributes = dir(obj) # Получаем атрибуты объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))] # Получаем методы объекта

    if obj_type in dir(builtins):
        module = 'builtins'
    else:
        module = obj_type.__module__

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info

# Пример класса
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        return f'Value: {self.value}'

if __name__ == '__main__':
    # Создаем объекты
    my_object1 = 42
    my_object2 = MyClass(11)
    # Проводим интроспекцию
    object_info1 = introspection_info(my_object1)
    object_info2 = introspection_info(my_object2)

    print("Информация о первом объекте:")
    pprint(object_info1)
    print("Информация о втором объекте:")
    pprint(object_info2)
    print("Информация о третьем объекте:")
    pprint(introspection_info("Я просто строка")) # Такой вариант тоже работает
