# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self):
        self.title = "Рисунок"

    def draw(self):
        print(f"Запуск отрисовки. {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Ручка. {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Карандаш. {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Рукоятка. {self.title}")

stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()