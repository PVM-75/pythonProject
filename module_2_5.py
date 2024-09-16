def get_matrix(n, m, value):

    matrix = [] # пустой список для матрицы

    for i in range(n): # цикл для строк
        row = [] # пустой список для строк
        for j in range(m): # цикл для столбцов
            row.append(value) # Заполняем строку значением
        matrix.append(row) # Добавляем заполненную строку в матрицу
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)