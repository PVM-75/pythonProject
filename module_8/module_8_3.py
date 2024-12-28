class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self.__is_valid_vin(__vin) == True:
            self.__vin = __vin
        if self.__is_valid_number(__numbers) == True:
            self.__numbers = __numbers


    def __is_valid_vin(self, vin):
        if isinstance(vin, int) == False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin < 1000000 or vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера') # формулировка не совсем верная, но не буду менять
        return True

    def __is_valid_number(self, numbers):
        if isinstance(numbers, str) == False:
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectVinNumber('Неверная длина номера')
        return True

if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')