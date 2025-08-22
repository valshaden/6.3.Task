# Основной файл main

from tkinter import *
from tkinter import ttk
import calculator_logic as c

def calc():
    second = float(entry.get())
    if oper == '+':
        result = c.add(first, second)
    elif oper == '-':
        result = c.subtract(first, second)
    elif oper == '*':
        result = c.multiply(first, second)
    elif oper == '/':
        result = c.divide(first, second)
    entry.delete(0, END)
    entry.insert(0, str(result))

def enter_number(number):
    entry.insert(END, number)

def set_operation(operation):
    global first
    global oper
    first = float(entry.get())
    oper = operation
    entry.delete(0, END)

def clear_entry():
    entry.delete(0, END)

# Создаем окно приложения
window = Tk()
window.title("Калькулятор")

entry = ttk.Entry(width=20)
entry.grid(row=0, column=0, columnspan=4, sticky="ew")

# Цифровые кнопки
ttk.Button(text="1", command=lambda: enter_number('1')).grid(row=1, column=0)
ttk.Button(text="2", command=lambda: enter_number('2')).grid(row=1, column=1)
ttk.Button(text="3", command=lambda: enter_number('3')).grid(row=1, column=2)
ttk.Button(text="4", command=lambda: enter_number('4')).grid(row=2, column=0)
ttk.Button(text="5", command=lambda: enter_number('5')).grid(row=2, column=1)
ttk.Button(text="6", command=lambda: enter_number('6')).grid(row=2, column=2)
ttk.Button(text="7", command=lambda: enter_number('7')).grid(row=3, column=0)
ttk.Button(text="8", command=lambda: enter_number('8')).grid(row=3, column=1)
ttk.Button(text="9", command=lambda: enter_number('9')).grid(row=3, column=2)
ttk.Button(text="0", command=lambda: enter_number('0')).grid(row=4, column=0)

# Кнопки арифметических операций
ttk.Button(text="+", command=lambda: set_operation('+')).grid(row=1, column=3)
ttk.Button(text="-", command=lambda: set_operation('-')).grid(row=2, column=3)
ttk.Button(text="*", command=lambda: set_operation('*')).grid(row=3, column=3)
ttk.Button(text="/", command=lambda: set_operation('/')).grid(row=4, column=3)

# Кнопка равно и очистки
ttk.Button(text="=", command=calc).grid(row=4, column=2)
ttk.Button(text="C", command=clear_entry).grid(row=4, column=1)

first = 0
oper = 0

window.mainloop()
