# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": 0, "bonus": 0}

    def set_income(self, wage, bonus):
        self.__income["wage"] = wage
        self.__income["bonus"] = bonus

    def get_income(self):
        return self.__income['wage'] + self.__income['bonus']

class Position(Worker):

    def get_full_name(self):
        print(f"Работник: {str(self.surname)} {str(self.name)} ; Должность: {self.position}")

    def get_total_income(self):
        print(f"Доход с учётом премии: {self.get_income()}")

worker1 = Position("Alex", "Turk", "Программист")
worker1.set_income(124500, 20000)
worker2 = Position("Anton", "Gavrilin", "Аналитик")
worker2.set_income(117990, 30000)

worker1.get_full_name()
worker1.get_total_income()

worker2.get_full_name()
worker2.get_total_income()
