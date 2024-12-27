class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'ФИО: {self.name}, Должность: {self.position}, Оклад: ${self.salary}'

class Manager(Employee):
    def __init__(self, name, position, salary, team_size):
        super().__init__(name, position, salary)
        self.team_size = team_size

    def __str__(self):
        return f"{super().__str__()}, Команда сотрудников: {self.team_size}"

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        for emp in self.employees:
            print(emp)

    def safe_to_file(self, filename):
        with open(filename, 'w') as file:
            for emp in self.employees:
                if isinstance(emp, Manager):
                    file.write(f'{emp.name}, {emp.position}, {emp.salary}, {emp.team_size} \n')
                else:
                    file.write(f'{emp.name}, {emp.position}, {emp.salary} \n')

    # на 27 минуте остановился