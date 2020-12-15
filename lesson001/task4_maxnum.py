# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

inputNumber = input("Введите целое положительное число: ")
power = inputNumber.__len__() - 1
number = int(inputNumber)

value = -1
while power > 0:
    temp = number // (10 ** power)
    number = number - temp * (10 ** power)
    power -= 1
    if temp > 0 and temp > value:
        value = temp
    elif temp > 0 and temp <= value:
        continue
    else:
        break

print(f"Самая большая цифра в числе {inputNumber}: {value}")
