# В файл runner_and_tournament я внес 2 исправления, иначе не работало...
# Неверные результаты будут при следующих условиях (одновременно):
# 1. При беге на короткие дистанции (3 и меньше),
# 2. Если при создании объекта Tournament передать в него сначала "медленного" бегуна, потом "быстрого"
import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    all_result = {}

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)
        # self.tournament = Tournament(90, )

    def test_1(self):
        tournament = Tournament(90, (self.runner_1, self.runner_3))
        results = tournament.start()
        self.all_result['test_1'] = results
        self.assertTrue(results[2] == 'Ник')

    def test_2(self):
        tournament = Tournament(90, (self.runner_2, self.runner_3))
        results = tournament.start()
        self.all_result['test_2'] = results
        self.assertTrue(results[2] == 'Ник')

    def test_3(self):
        tournament = Tournament(90, (self.runner_1, self.runner_2, self.runner_3))
        results = tournament.start()
        self.all_result['test_3'] = results
        self.assertTrue(results[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_result.items():
            print(f'{value}')

# Запускаем тесты
if __name__ == "__main__":
    unittest.main()