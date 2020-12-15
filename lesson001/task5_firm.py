# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print("(Формула выручки → Цена * Количество проданных товаров)")
price = int(input("Введите значение цены на товар: "))
count = int(input("Введите количество проданных товаров: "))
markup = int(input("Введите значение наценки: "))

gain = price * count
profit = markup * count
costPrice = price - markup
print(f"Выручка фирмы: {gain}")
print(f"Прибыль фирмы: {profit}")

cost = int(input("Введите значение издержки фирмы: "))

if gain > cost:
    efficiency = (gain - costPrice * count) * 100 / gain;
    print("Финансовый результат: прибыль")
    print(f"Рентабельность выручки: {efficiency:.2f}%")
    countEmployee = int(input("Введите число сотрудников: "))
    profitPerson = profit / countEmployee
    print(f"Прибыль в расчёте на одного сотрудника: {profitPerson:.2f}")
elif gain < cost:
    print("Финансовый результат: убыток")
else:
    print("Финансовый результат: ...")