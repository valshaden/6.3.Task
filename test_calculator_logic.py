# 5.3.1. Файл с функциями
# 5.3.2. Основной файл main
# 5.3.3. Метод grid 
# 5.3.4. Создаем интерфейс
# 5.3.5. Отладка программы
# 5.3.6. Unit-тесты

# Юнит тесты создаем файл test_calculator_logic.py

import calculator_logic as calc

def test_add():
    assert calc.add(10, 5) == 15
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_subtract():
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(-1, -1) == 0

def test_multiply():
    assert calc.multiply(10, 5) == 50
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(-1, -1) == 1

def test_divide():
    assert calc.divide(10, 5) == 2

    # Проверка исключения при делении на ноль
    #try:
    #    calc.divide(10, 0)
    #    assert False  # Эта строка не должна выполняться, если исключение произошло
    #except ValueError:
    #    assert True  # Если исключение произошло, тест пройден

    assert calc.divide(-1, 1) == -1
    assert calc.divide(-1, -1) == 1

test_add()
test_subtract()
test_multiply()
test_divide()
print("Все тесты пройдены успешно!")
