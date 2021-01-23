# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivZeroExc(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    nominator = input("Введите числитель: ")
    denominator = input("Введите знаменатель: ")
    if not nominator.isdigit() or not denominator.isdigit():
        continue
    nominator, denominator = (int(nominator), int(denominator))
    try:
        if denominator == 0:
            raise DivZeroExc("Исключение. Деление на 0")
        result = nominator / denominator
        print(f"Результат деления: {result:.2f}")
    except DivZeroExc as err:
        print(err)
    except Exception:
        print("Что-то пошло не так...")
    break
