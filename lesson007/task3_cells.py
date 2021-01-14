# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны
# применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
# деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества
# ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
# количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
# деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Заменить __truediv__ на __floordiv__ (или добавить ?)


class Cell:
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = int(number) if str(number).isdigit() and int(number) > 0 else 1

    def __str__(self):
        return "*" * self.number

    def __add__(self, other):
        if type(other) != Cell:
            raise TypeError
        cell_number = self.number + other.number
        return Cell(cell_number)

    def __sub__(self, other):
        if type(other) != Cell:
            raise TypeError
        if self.number <= other.number:
            raise ValueError
        cell_number = self.number - other.number
        return Cell(cell_number)

    def __mul__(self, other):
        if type(other) != Cell:
            raise TypeError
        cell_number = self.number * other.number
        return Cell(cell_number)

    def __floordiv__(self, other):
        if type(other) != Cell:
            raise TypeError
        if (self.number - other.number) < 1:
            raise ValueError
        cell_number = self.number // other.number
        return Cell(cell_number)

    def __truediv__(self, other):
        if type(other) != Cell:
            raise TypeError
        if (self.number - other.number) < 1:
            raise ValueError
        cell_number = self.number // other.number
        return Cell(cell_number)

    def make_order(self, split_count):
        if split_count < 1:
            split_count = 1
        order = ""
        counter = 1
        while True:
            if split_count * (counter - 1) > self.number:
                break
            row_count = split_count if self.number > split_count * counter else self.number - split_count * (counter - 1)
            order += "*" * row_count
            order += "\n"
            counter += 1
        return order


cell_1 = Cell(12)
cell_2 = Cell(16)

cell_3 = cell_1 + cell_2
print(f"sum order for new cell:\n{cell_3.make_order(5)}")

cell_1.number = 15
cell_2.number = 8
cell_3 = cell_1 - cell_2
print(f"sub order for new cell:\n{cell_3.make_order(3)}")

cell_1.number = 7
cell_2.number = 5
cell_3 = cell_1 * cell_2
print(f"multiply order for new cell:\n{cell_3.make_order(8)}")

cell_1.number = 29
cell_2.number = 3
cell_3 = cell_1 / cell_2
print(f"div order for new cell:\n{cell_3.make_order(4)}")
