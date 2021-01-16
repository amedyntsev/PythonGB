# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, real, img):
        if type(real) != float or type(img) != float:
            raise TypeError
        self.real = real
        self.img = img

    def __add__(self, other):
        if type(other) != ComplexNumber:
            raise TypeError
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        if type(other) != ComplexNumber:
            raise TypeError
        return ComplexNumber((self.real * other.real - self.img * other.img),
                             (self.real * other.img + other.real * self.img))

    def __str__(self):
        return f"{self.real:.2f} + {self.img:.2f}i"


cn_1 = ComplexNumber(25.0, -17.1)
cn_2 = ComplexNumber(-2.2, 13.8)
cn_3 = cn_1 + cn_2
cn_4 = cn_1 * cn_2
print(f"Комплексные числа: ({cn_1}) и ({cn_2})\nСумма чисел: {cn_3}\nПроизведение чисел: {cn_4}")
