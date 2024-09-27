import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_result(result):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, result)

def add():
    num1, num2 = get_values()
    result = num1 + num2
    insert_result(result)

def sub():
    num1, num2 = get_values()
    result = num1 - num2
    insert_result(result)

def mul():
    num1, num2 = get_values()
    result = num1 * num2
    insert_result(result)

def div():
    num1, num2 = get_values()
    result = num1 / num2
    insert_result(result)

window = tk.Tk()
window.title('Калькуль')
window.geometry('320x210')
window.resizable(False, False)
button_add = tk.Button(window, text = '+', width=4, height=2, command=add)
button_add.place(x=5, y=105)
button_sub = tk.Button(window, text = '-', width=4, height=2, command=sub)
button_sub.place(x=55, y=105)
button_mul = tk.Button(window, text = '*', width=4, height=2, command=mul)
button_mul.place(x=105, y=105)
button_div = tk.Button(window, text = '/', width=4, height=2, command=div)
button_div.place(x=155, y=105)
number1_entry = tk.Entry(window, width=50)
number1_entry.place(x=5, y=30)
number2_entry = tk.Entry(window, width=50)
number2_entry.place(x=5, y=80)
answer_entry = tk.Entry(window, width=50)
answer_entry.place(x=5, y=180)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=5, y=5)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=5, y=55)
answer = tk.Label(window, text='Ответ:')
answer.place(x=5, y=155)
window.mainloop()