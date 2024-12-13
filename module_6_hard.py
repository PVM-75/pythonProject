from math import pi
from math import sqrt

class Figure:
    sides_count = 0 # количество сторон

    def __init__(self, color, sides, filled = False):
        self.__color = list(color)
        self.__sides = sides # Длинна(ы) сторон
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, colors):
        # print(colors)
        if colors[0] >= 0 and colors[0] <= 255 and colors[1] >= 0 and colors[1] <= 255 and colors[2] >= 0 and colors[2] <= 255:
            return True
        else:
            return False
        # return valid

    def set_color(self, *colors):
        if self.__is_valid_color(colors) == True:
            self.__color = list(colors)

    def __is_valid_sides(self, new_sides):
        valid = True
        if len(new_sides) == self.sides_count:
            for item in new_sides:
                if isinstance(item, int) and item > 0:
                    continue
                else:
                    valid = False
                    break
        else:
            valid = False
        return valid

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) == True:
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides) # не работает, переделать self.__sides на список

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled = False):
        if len(sides) != 1:
            sides = [1]
        else:
            sides = list(sides)
        self.__radius = round((sum(sides) / (pi * 2)), 2)
        super().__init__(color, sides, filled)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return round((self.__radius ** 2 * pi), 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled = False):
        if len(sides) != 3:
            sides = [1, 1, 1]
        else:
            sides = list(sides)
        super().__init__(color, sides, filled)

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2 # полупериметр
        s = round((sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))), 2)
        return s

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled = False):
        if len(sides) != 1:
            sides = [1, 1, 1]
        else:
            sides = list(sides * 12)
        super().__init__(color, sides, filled)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3 # взял элемент списка [0] потому что все элементы равны между собой

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    print('Проверка на изменение цветов')
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    print(cube1.sides_count)

    # Проверка на изменение сторон:
    print('Проверка на изменение сторон')
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print('Проверка периметра (круга), это и есть длина:')
    print(len(circle1))

    # Проверка объёма (куба):
    print('Проверка объёма (куба):')
    print(cube1.get_volume())

    # мои проверки
    print('Дополнительные проверки (сверх задания)')
    print(circle1.get_radius())
    print(circle1.get_square())
    tr1 = Triangle((200, 200, 100), 10, 6)
    tr2 = Triangle((200, 200, 100), 10, 6, 6)
    print(tr1.get_sides())
    print(tr2.get_sides())
    print(tr2.get_square())