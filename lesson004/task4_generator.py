# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.


def split_numbers(string):
    result = []
    for key, value in enumerate(string.split()):
        if value.isdigit():
            result.append(int(string.split()[key]))
    return result


def func(numbers):
    return [element for element in numbers if numbers.count(element) == 1]


while True:
    numbers = split_numbers(input("Введите числа разделённые пробелом: "))
    if len(numbers) < 1:
        continue
    break

print(f"Элементы не имеющие повторений: {func(numbers)}")