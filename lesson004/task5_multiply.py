# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

result = [element for element in range(100, 1001) if element % 2 == 0]
print(f"Чётные числа от 100 до 1000: {result}")
print(f"Произведение всех элементов: {reduce(lambda x,y: x * y, result)}")