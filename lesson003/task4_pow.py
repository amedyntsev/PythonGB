# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    y = int(y)
    return x ** y

def my_func2(x, y):
    y = int(y)
    result = x
    if y < 2:
        return result
    while y > 1:
        y -= 1
        result *= x
    return result

# примеры
print(f"Func1: {my_func(14,3)}")
print(f"Func2: {my_func2(11,4)}")


