class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.eatable == True:
            print(<self.name>, 'съел ', <food.name>)
            self.fed = True
        else:
            print(<self.name>, 'не стал есть', <food.name>)


class Plant:
    def __init__(self, name):
        self.name = name
        self.eatable = True

class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    eatable = False
    pass


class Fruit(Plant):
    eatable = True
    pass

if __name__ == '__main__':
    # Выполняемый код(для проверки):
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    # a1.eat(p1)
    # a2.eat(p2)
    # print(a1.alive)
    # print(a2.fed)