# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не
# остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.


class NotNumberExc(Exception):
    def __init__(self, txt):
        self.txt = txt


def is_digit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


list_numbers = []
try:
    while True:
        value = input("Введите число для списка: ")
        if value == "stop":
            print(f"Список чисел: {list_numbers}")
            break
        if is_digit(value):
            list_numbers.append(int(value))
        else:
            raise NotNumberExc("Исключение. Введённое значение не является числом")
except NotNumberExc as err:
    print(err)
