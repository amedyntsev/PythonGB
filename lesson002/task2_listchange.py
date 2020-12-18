# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print("Для завершения ввода элементов в список введите 'exit'")

userList = []
count = 0
while True:
    value = input(f"Введите значение в список (количество эл-в в списке: {count}): ")
    if value == "exit":
        break
    else:
        userList.append(value)
        count += 1

pointer = 0
print(f"Список до перестановки:  {userList}")
while True:
    tmp = userList.pop(pointer + 1)
    userList.insert(pointer, tmp)
    if pointer < (len(userList) - 3):
        pointer += 2
    else:
        break
print(f"Список после перестановки:  {userList}")