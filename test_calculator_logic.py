# Юнит тесты

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

def test_square():
    assert calc.square(5) == 25
    assert calc.square(-3) == 9
    assert calc.square(0) == 0

test_add()
test_subtract()
test_multiply()
test_divide()
test_square()
print("Все тесты пройдены успешно!")
