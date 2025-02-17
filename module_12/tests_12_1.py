import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj1 = Runner('Vasya')
        for i in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 50)

    def test_run(self):
        obj2 = Runner('Fedya')
        for i in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    def test_challenge(self):
        obj3 = Runner('Olya')
        for i in range(10):
            obj3.walk()
        obj4 = Runner('Gena')
        for i in range(10):
            obj4.run()
        self.assertNotEqual(obj3.distance, obj4.distance)

if __name__ == '__main__':
    unittest.main()
    # obj1 = Runner('Vasya')
    # for i in range(10):
    #     obj1.run()
    # print(obj1.distance)
    # obj2 = Runner('Fedya')
    # for i in range(10):
    #     obj2.walk()
    # print(obj2.distance)