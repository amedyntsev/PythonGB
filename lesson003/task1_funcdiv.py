# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide(var1, var2):
    if(var2 == 0):
        print("Ошибка. Деление на ноль")
    else:
        return var1 / var2

print("——————————————————————————————————")
print("+ Введите два числа для деления +")
while True:
    var1 = input("Число 1: ")
    var2 = input("Число 2: ")
    if not var1.isdigit() or not var2.isdigit():
        continue
    var1 = int(var1)
    var2 = int(var2)
    result = divide(var1,var2)
    if result is None:
        continue
    else:
        print(f"Деление var1 на var2: {result:.2f}")
        break