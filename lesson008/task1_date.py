# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def split_date(cls, date):
        day, month, year = str(date).split("-") if len(str(date).split("-")) == 3 else (0, 0, 0)
        validate = cls.validate_date(day=day, month=month, year=year)
        if validate != 1:
            return validate
        return f"Дата корректна. День: {day} ; Месяц: {month} ; Год: {year} "

    @staticmethod
    def validate_date(**kwargs):
        if False in [str(val).isdigit() for val in kwargs.values()]:
            return f"Ошибка. В дате содержатся символы → {kwargs}"
        if not int(kwargs["day"]) in [day for day in range(1,32)]:
            return f"Ошибка. День даты выходит за пределы диапазона от 1 до 31 → {kwargs['day']}"
        if not int(kwargs["month"]) in [month for month in range(1,13)]:
            return f"Ошибка. Месяц выходит за пределы диапазона от 1 до 12 → {kwargs['month']}"
        if not int(kwargs["year"]) in [month for month in range(1,3001)]:
            return f"Ошибка. Год выходит за пределы диапазона от 1 до 3000 → {kwargs['year']}"
        return 1


date = Date("12a-06b-1995d")
print(date.split_date(date.date_string))
date = Date("27-13-1992")
print(date.split_date(date.date_string))
date = Date("30-11-2002")
print(date.split_date(date.date_string))
date = Date("32-09-1989")
print(date.split_date(date.date_string))
date = Date("01-02-2015")
print(date.split_date(date.date_string))
date = Date("09-04-2015")
print(date.split_date(date.date_string))
date = Date("02-11-3020")
print(date.split_date(date.date_string))
date = Date("12a-06b-1995d-o0")
print(date.split_date(date.date_string))
