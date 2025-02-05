class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(*participants) # Добавил *

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name # Добавил .name
                    place += 1
                    self.participants.remove(participant)

        return finishers

if __name__ == '__main__': # Этот блок работает с исправлениями
    runner_1 = Runner('Усейн', 10)
    runner_2 = Runner('Андрей', 9)
    runner_3 = Runner('Ник', 3)
    tournament = Tournament(90, (runner_1, runner_3))
    result = tournament.start()
    print(result)