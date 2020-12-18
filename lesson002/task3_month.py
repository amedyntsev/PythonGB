# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = -1
while True:
    month = input("Введите месяц в виде целого числа от 1 до 12: ")
    if not month.isdigit or month == '':
        continue

    print(month)
    month = int(month)
    if month < 1 or month > 12:
        continue
    break

# Решение через LIST

monthList = [[1,2,12], [3,4,5], [6,7,8], [9,10,11]]

seasonId = 0
for season in monthList:
    seasonId += 1
    if month in season:
        break

seasonName = ""
if seasonId == 1:
    seasonName = "Зима"
elif seasonId == 2:
    seasonName = "Весна"
elif seasonId == 3:
    seasonName = "Лето"
else:
   seasonName = "Осень"
print(f"Решение с помощью списка, сезон: {seasonName}")

# Решение через DICT

monthDict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
print(f"Решение с помощью словаря, сезон: {monthDict[month]}")

# Смешанное решение

monthOther = {"Зима":[1,2,12], "Весна":[3,4,5], "Лето":[6,7,8], "Осень":[9,10,11]}
while len(monthOther) > 0:
    if month in monthOther[list(monthOther.keys())[0]]:
        print(f"Смешанное решение, сезон: {monthDict[month]}")
        break
    else:
        monthOther.pop(list(monthOther.keys())[0])