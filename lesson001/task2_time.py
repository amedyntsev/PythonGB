# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

timeseconds = int(input("Введите количество секунд: "))

hours = timeseconds // 3600
minutes = timeseconds // 60 - hours * 60
seconds = timeseconds - (hours * 3600 + minutes * 60)
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
