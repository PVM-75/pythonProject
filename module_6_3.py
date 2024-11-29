from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_x = self.cords[0] + dx * self.speed
        new_y = self.cords[1] + dy * self.speed
        new_z = self.cords[2] + dz * self.speed
        if new_z > 0:
            self.cords[0] = new_x
            self.cords[1] = new_y
            self.cords[2] = new_z
        else:
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f"X: {self.cords[0]}, Y: {self.cords[1]}, Z: {self.cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    num_of_eggs = randint(1, 4)

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        print(f"Here are(is) {self.num_of_eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.cords[2] -= int(dz * (self.speed / 2))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

if __name__ == "__main__":
    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak() # этой функции нет в тех. задании, добавил в класс Animal
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()