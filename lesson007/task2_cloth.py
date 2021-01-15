# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом
# уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


def general_consumption(*args):
    consumption = 0
    for value in args:
        if type(value) != Coat and type(value) != Suit:
            continue
        consumption += value.consumption
    print(f"Общий расход ткани: {consumption:.2f}")


class Cloth(ABC):
    @abstractmethod
    def consumption_cloth(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return self.__size / 6.5 + 0.5

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 200:
            self.__size = 200
        else:
            self.__size = size

    def consumption_cloth(self):
        return f"Для пальто размера {self.__size} расход ткани = {self.consumption:.2f}"


class Suit(Cloth):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        return 2 * self.__height + 0.3

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 120:
            self.__height = 120
        elif height > 220:
            self.__height = 220
        else:
            self.__height = height

    def consumption_cloth(self):
        return f"Для костюма рассчитанного на рост {self.__height} расход ткани = {self.consumption:.2f}"


coat = Coat(20)
suit = Suit(240)

print(coat.consumption_cloth())
print(suit.consumption_cloth())

coat.size = 120
suit.height = 90

print(coat.consumption_cloth())
print(suit.consumption_cloth())

suit2 = Suit(150)
print(suit2.consumption_cloth())

general_consumption(coat, suit, suit2)
