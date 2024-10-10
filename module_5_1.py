class House:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.floor:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(f'Такого этажа в "{self.name}" не существует!') # Немного отступил от условия задачи, так красивее )


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# print(h1.name, h1.floor)
# print(h2.name, h2.floor)
h1.go_to(5)
h2.go_to(10)