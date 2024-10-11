class House:
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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))