import tkinter as tk

def get_values():
    num1 = float(number1_entry.get()) / 100
    num2 = float(number2_entry.get()) / 100
    num3 = float(number3_entry.get()) * 1000
    return num1, num2, num3

def get_result():
    orig_percent, result_percent, result_volume = get_values()
    result = round(result_volume * result_percent / orig_percent, 2)
    water = round(result_volume - result, 2)
    insert_result(result, water)

def insert_result(result, water):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, result)
    water_entry.delete(0, 'end')
    water_entry.insert(0, water)

# Основное окно
window = tk.Tk()
window.title('Огородный калькуль')
window.geometry('320x320')
window.resizable(False, False)

number1 = tk.Label(window, text='Введите концентрацию исходного вещества (%):')
number1.place(x=5, y=5)
number1_entry = tk.Entry(window, width=50) # Окно ввода 1
number1_entry.place(x=5, y=30)

number2 = tk.Label(window, text='Введите концентрация конечного раствора (%):')
number2.place(x=5, y=55)
number2_entry = tk.Entry(window, width=50) # Окно ввода 2
number2_entry.place(x=5, y=80)

number3 = tk.Label(window, text='Введите количество конечного раствора (литров):')
number3.place(x=5, y=105)
number3_entry = tk.Entry(window, width=50) # Окно ввода 3
number3_entry.place(x=5, y=130)

button_add = tk.Button(window, text = 'Рассчитать', width=42, height=2, command=get_result) # Кнопка сложения
button_add.place(x=5, y=155)

answer = tk.Label(window, text='Исходного раствора (мл):')
answer.place(x=5, y=200)
answer_entry = tk.Entry(window, width=50) # Окно вывода
answer_entry.place(x=5, y=230)

water = tk.Label(window, text='Воды (мл):')
water.place(x=5, y=250)
water_entry = tk.Entry(window, width=50) # Окно вывода
water_entry.place(x=5, y=280)

window.mainloop()