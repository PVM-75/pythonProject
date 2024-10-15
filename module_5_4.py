class House:
    houses_history = []

    def __new__(cls, *args):
        instance = super(House, cls).__new__(cls)
        if args:  # Проверяем, что переданы аргументы
            cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.floor:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(f'Такого этажа в "{self.name}" не существует!')  # Немного отступил от условия задачи, так красивее )

    def __len__(self):
        return self.floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floor}'

    def __eq__(self, other):
        return self.floor == other.floor

    def __lt__(self, other):
        return self.floor < other.floor

    def __le__(self, other):
        return self.floor <= other.floor

    def __gt__(self, other):
        return self.floor > other.floor

    def __ge__(self, other):
        return self.floor >= other.floor

    def __ne__(self, other):
        return self.floor != other.floor

    def __add__(self, value):
        if isinstance(self, House) and isinstance(value, int):  # Проверяем, что value - это число
            return House(self.name, self.floor + value)  # Возвращаем новый объект House с увеличенным количеством этажей
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(self, House) and isinstance(value, int):  # Проверяем, что value - это число
            self.floor += value  # Увеличиваем этажи этого объекта
            return self  # Возвращаем сам объект
        return NotImplemented

    def __radd__(self, value):
        if isinstance(self, House) and isinstance(value, int):
            return House(self.name, self.floor + value)
        return NotImplemented

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории