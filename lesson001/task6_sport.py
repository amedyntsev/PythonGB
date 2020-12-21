# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

while True:
    distanceA = int(input("Начальный результат в км: "))
    distanceB = int(input("Целевой результат в км: "))

    if distanceA >= distanceB:
        print("Ошибка ввода. Начальный результат должен быть меньше целевого – повторите попытку")
        continue

    daysCount = 1
    while distanceA < distanceB:
        distanceA = distanceA + distanceA * 0.1
        daysCount += 1

    print(f"Количество дней, которое требуется спортсмену, чтобы достичь целевого результата: {daysCount}")
    break