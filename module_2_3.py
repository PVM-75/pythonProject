my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_list = 0
while index_list < len(my_list):
    if my_list[index_list] == 0:
        index_list = index_list + 1
        # continue
    elif my_list[index_list] > 0:
        print(my_list[index_list])
        index_list = index_list + 1
    else:
        break
print('Приложение завершено')