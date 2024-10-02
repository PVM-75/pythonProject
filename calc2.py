import tkinter as tk

num_1 = ''
num_2 = ''
action = ''

def insert_num(button_num='1'):
    global num_1, num_2, action
    if action == '+' or  action == '-' or action == '*' or action == '/':
        num_2 = num_2 + button_num
        insert_result(num_2)
        print(num_2)
    else:
        num_1 = num_1 + button_num
        insert_result(num_1)
        print(num_1)
    # return num_1, num_2

def insert_result(ins): # Временная функция
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, ins)



window = tk.Tk()
window.title('Калькуль')
window.geometry('320x400')
window.resizable(False, False)

answer_entry = tk.Entry(window, width=50) # Окно ввода-вывода
answer_entry.place(x=5, y=5)

# Кнопки ввода цифр

button_1 = tk.Button(window, text = '1', width=4, height=2, command=insert_num) # Кнопка 1
button_1.place(x=5, y=55)
button_2 = tk.Button(window, text = '2', width=4, height=2) # Кнопка вычитания
button_2.place(x=55, y=55)
button_3 = tk.Button(window, text = '3', width=4, height=2) # Кнопка умножения
button_3.place(x=105, y=55)
button_add = tk.Button(window, text = '+', width=4, height=2) # Кнопка сложения
button_add.place(x=155, y=55)

window.mainloop()