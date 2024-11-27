class Vehicle:
    color_variants = ["blue", "green", "black", "white"]
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.color = color

    def get_model(self):
        print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Мощность: {self.__engine_power}")

    def get_color(self):
        print(f"Цвет: {self.color}")

    def print_info(self):
        print(f"Модель: {self.__model}")
        print(f"Мощность: {self.__engine_power}")
        print(f"Цвет: {self.color}")
        print(f"Владелец: {self.owner}")

class Sedan(Vehicle):
    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)
        self.__passengers_limit = 5



if __name__ == "__main__":
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    # vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    # vehicle1.set_color('Pink')
    # vehicle1.set_color('BLACK')
    # vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()

    # Это мои проверки
    # vehicle1.get_model()
    # vehicle1.get_horsepower()