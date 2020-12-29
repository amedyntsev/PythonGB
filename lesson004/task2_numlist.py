# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.


def split_numbers(string):
    result = []
    for key, value in enumerate(string.split()):
        if value.isdigit():
            result.append(int(string.split()[key]))
    return result


def func(numbers):
    return [element for key, element in enumerate(numbers) if key > 0 and numbers[key] > numbers[key - 1]]


while True:
    numbers = split_numbers(input("Введите числа разделённые пробелом: "))
    if len(numbers) < 1:
        continue
    break

numbers = func(numbers)
print(f"Значения больше предыдущих: {numbers}")