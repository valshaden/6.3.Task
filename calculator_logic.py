# Файл с функциями

# Калькулятор в двух файлах с интерфейсом
# файл с функциями calculator_logic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
