total_sum = 0

def calculate_structure_sum(data):
    global total_sum

    if isinstance(data, list) or isinstance(data, tuple):
        if isinstance(data[0], (int, float)):
            for i in data:
                total_sum += i
        elif isinstance(data[0], str):
            for i in data:
                total_sum += len(i)
        for item in data:
            calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)
    elif isinstance(data, str):
        total_sum += len(data)
    elif isinstance(data, (int, float)):
        total_sum += data

    return total_sum

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99