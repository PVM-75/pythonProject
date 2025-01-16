from threading import Thread, Lock
from random import randint
from queue import Queue
from time import sleep

class Table:
    def __init__(self, tables_num):
        self.guest = None
        self.tables_num = tables_num

class Guest(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        self.wait_time = randint(3, 10)
        sleep(self.wait_time)
        # print(f'{self.name} покинул(а) стол') # есть в задании?

class Cafe:
    def __init__(self, *args):
        self.q = Queue()
        self.tables = []
        for item in args:
            self.tables.append(item)
        self.lock = Lock()  # Для синхронизации доступа к столам

    def guest_arrival(self, *guests):
        for guest in guests:
            assigned_table = False
            with self.lock:
                for table in self.tables:
                    if table.guest is None: # and guest.have_table == False:
                        table.guest = guest
                        assigned_table = True
                        guest.start()
                        # guest.join()
                        print(f'{guest.name} сел(а) за стол номер {table.tables_num}')
                        break
                if not assigned_table:
                    self.q.put(guest)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while True:
            all_tables_free = True  # Переменная для отслеживания, свободны ли все столы
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')  # Сообщение о том, что гость покинул стол
                    table.guest = None
                    print(f'Стол номер {table.tables_num} стал свободным')  # Сообщение о том, что стол освободился
                # Проверяем, свободен ли стол
                if table.guest is not None:
                    all_tables_free = False  # Если есть хотя бы один стол с гостем, устанавливаем False

            if all_tables_free:  # Если все столы свободны, выходим из цикла
                print("Все столы свободны. Все посетители обслужены.")
                break  # Завершение работы программы

            if not self.q.empty():  # Если есть очередь, передаем гостей за столы
                for table in self.tables:
                    if table.guest is None:
                        table.guest = self.q.get()
                        print(f'{table.guest.name} вышел из очереди и сел(а) за стол номер {table.tables_num}')
                        table.guest.start()  # Запуск нового потока для нового гостя
                        break  # Прерываем цикл, чтобы обновить только один стол

            sleep(0.5)  # Небольшая задержка для предотвращения избыточного использования ЦП

if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
    # Проверка, что все столы свободны:
    for table in cafe.tables:
        print(f'Стол {table.tables_num} состояние: {table.guest}')
