# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def factorial(number):
    fact = 1
    pointer = 1
    while pointer <= number:
        yield fact
        pointer += 1
        fact *= pointer


while True:
    number = input("Введите целое положительное число (до 10): ")
    if not number.isdigit():
        continue
    number = int(number)
    if number < 0 or number > 10:
        continue
    break


fact = factorial(number)
for element in fact:
    print(f"value: {element}")
