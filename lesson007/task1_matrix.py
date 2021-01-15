# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += "".join(f"{e:>4}" for e in row)
            result += "\n"
        return result

    def __add__(self, other):
        if type(other) != Matrix:
            return
        if len(other.matrix) != len(self.matrix):
            return
        result_list = []
        for key, value in enumerate(other.matrix):
            if len(value) != len(self.matrix[key]):
                return
            row = list(map(lambda x, y: x + y, value, self.matrix[key]))
            result_list.append(row)
        result = Matrix(result_list)
        return result


# примеры
matrix_1 = Matrix([[11, 2, 66], [53, 4, -13], [25, 7, 11]])
matrix_2 = Matrix([[14, 21, 7], [5, 16, -7], [2, 72, 7]])
matrix_3 = Matrix([[19, 1, -7], [-4, 77, 9], [-5, -20, -7]])

try:
    matrix_sum = matrix_1 + matrix_2 + matrix_3
    print(matrix_sum)
except Exception:
    print("Что-то пошло не так...")
