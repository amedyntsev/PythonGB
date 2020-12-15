# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

var1 = "test value"
print(f"var1: {var1}")

var2 = 66.1
print(f"var2: {var2}")

userIntInput1 = int(input("Введите число 1: "))
userIntInput2 = int(input("Введите число 2: "))
userStrInput1 = input("Введите что-нибудь 1: ")
userStrInput2 = input("Введите что-нибудь 2: ")

print(f"(f-string) Число, которое вы ввели 1: {userIntInput1}")
print(f"(f-string) Число, которое вы ввели 2: {userIntInput2}")
print(f"(f-string) Текст, который вы ввели 1: {userStrInput1}")
print(f"(f-string) Текст, который вы ввели 2: {userStrInput2}")
