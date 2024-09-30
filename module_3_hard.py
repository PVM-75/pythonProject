total_sum = 0

def calculate_structure_sum(data):
    global total_sum

    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for item in data:
            if isinstance(item, (int, float)):
                total_sum += item
            elif isinstance(item, str):
                total_sum += len(item)
            else:
                calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(key, (int, float)):
                total_sum += key
            elif isinstance(key, str):
                total_sum += len(key)
            else:
                calculate_structure_sum(key)
        # for value in data.items():
            if isinstance(value, (int, float)):
                total_sum += value
            elif isinstance(value, str):
                total_sum += len(value)
            else:
                calculate_structure_sum(value)
    elif isinstance(data, str):
        total_sum += len(data)
    elif isinstance(data, int) or isinstance(data, float):
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
print(result)