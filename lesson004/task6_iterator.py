# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import count, cycle


def is_digit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# Script A
min_edge = -10
max_edge = 10
while True:
    number = input("Укажите число с которого начать генерацию целых чисел  (от -10 до 10): ")
    if not is_digit(number) or not (min_edge < int(number) < max_edge):
        continue
    break
number = int(number)
resultA = []
for i in count(number):
    if i > max_edge:
        break
    else:
        resultA.append(i)
print(f"Script A: {resultA}")

print("–––––––––––––––––––––––––––")

#  Script B
def_list = list(range(4))
length = 15
generate_list = []
for key, value in enumerate(cycle(def_list)):
    generate_list.append(value)
    if key > length:
        break
print(f"Script B: {generate_list}")
