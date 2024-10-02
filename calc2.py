import tkinter as tk

num_1 = ''
num_2 = ''
action = ''
result = 0

def insert_num(button_num):
    global num_1, num_2, action

    if action == '+' or  action == '-' or action == '*' or action == '/':
        num_2 = num_2 + button_num
        insert_result(num_2)
        # print(num_2)
    else:
        num_1 = num_1 + button_num
        insert_result(num_1)
        # print('Number1:', num_1)
    # return num_1, num_2

def insert_action(act):
    global action
    action = act
    print(action)

def get_result():
    global num_1, num_2, action, result
    if action == '+':
        result = float(num_1) + float(num_2)
    elif action == '-':
        result = float(num_1) - float(num_2)
    elif action == '*':
        result = float(num_1) * float(num_2)
    elif action == '/':
        if int(num_2) == 0:
            result = 'Error'
        else:
            result = float(num_1) / float(num_2)
    insert_result(result)

def reset():
    global num_1, num_2, action, result
    num_1 = ''
    num_2 = ''
    action = ''
    result = 0
    answer_entry.delete(0, 'end')

def insert_result(ins): # Временная функция
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, ins)

window = tk.Tk()
window.title('Калькуль')
window.geometry('320x400')
window.resizable(False, False)

answer_entry = tk.Entry(window, width=17, font=('Arial', 24), justify='right') # Окно ввода-вывода
answer_entry.place(x=5, y=5)

# Кнопка сброса
button_reset = tk.Button(window, text = 'C', width=6, height=3, command=lambda: reset()) # Кнопка 1
button_reset.place(x=5, y=55)
# Кнопки ввода цифр

button_1 = tk.Button(window, text = '1', width=6, height=3, command=lambda: insert_num('1')) # Кнопка 1
button_1.place(x=5, y=115)
button_2 = tk.Button(window, text = '2', width=6, height=3, command=lambda: insert_num('2')) # Кнопка 2
button_2.place(x=65, y=115)
button_3 = tk.Button(window, text = '3', width=6, height=3, command=lambda: insert_num('3')) # Кнопка 3
button_3.place(x=125, y=115)
button_4 = tk.Button(window, text = '4', width=6, height=3, command=lambda: insert_num('4')) # Кнопка 4
button_4.place(x=5, y=175)
button_5 = tk.Button(window, text = '5', width=6, height=3, command=lambda: insert_num('5')) # Кнопка 5
button_5.place(x=65, y=175)
button_6 = tk.Button(window, text = '6', width=6, height=3, command=lambda: insert_num('6')) # Кнопка 6
button_6.place(x=125, y=175)
button_7 = tk.Button(window, text = '7', width=6, height=3, command=lambda: insert_num('7')) # Кнопка 7
button_7.place(x=5, y=235)
button_8 = tk.Button(window, text = '8', width=6, height=3, command=lambda: insert_num('8')) # Кнопка 8
button_8.place(x=65, y=235)
button_9 = tk.Button(window, text = '9', width=6, height=3, command=lambda: insert_num('9')) # Кнопка 9
button_9.place(x=125, y=235)
button_neg = tk.Button(window, text = '+/1', width=6, height=3, command=lambda: insert_num('7')) # Кнопка 4
button_neg.place(x=5, y=295)
button_0 = tk.Button(window, text = '0', width=6, height=3, command=lambda: insert_num('0')) # Кнопка 0
button_0.place(x=65, y=295)
button_point = tk.Button(window, text = '.', width=6, height=3, command=lambda: insert_num('.')) # Кнопка 6
button_point.place(x=125, y=295)

# Кнопки функций
button_add = tk.Button(window, text = '+', width=6, height=3, command=lambda: insert_action('+')) # Кнопка сложения
button_add.place(x=185, y=115)
button_sub = tk.Button(window, text = '-', width=6, height=3, command=lambda: insert_action('-')) # Кнопка вычитания
button_sub.place(x=185, y=175)
button_mul = tk.Button(window, text = '*', width=6, height=3, command=lambda: insert_action('*')) # Кнопка умножения
button_mul.place(x=185, y=235)
button_div = tk.Button(window, text = '/', width=6, height=3, command=lambda: insert_action('/')) # Кнопка деления
button_div.place(x=185, y=295)

# Кнопка равно
button_answer = tk.Button(window, text = '=', width=31, height=2, command=lambda: get_result()) # Кнопка Равно
button_answer.place(x=5, y=355)

window.mainloop()