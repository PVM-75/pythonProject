def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function() # Вызываю вункцию test_function, чтобы отработала функция inner_function
inner_function() # Вызов функции выдает ошибку, так как имя данной функции за пределами области видимости