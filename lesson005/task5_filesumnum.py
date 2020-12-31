# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


from random import random
from functools import reduce

with open("task_5.txt", "w", encoding="utf-8") as f:
    rand = int(random() * 30)
    numbers = " ".join([f"{element}" for element in range(0,rand)])
    print(numbers, file=f)

with open("task_5.txt", "r", encoding="utf-8") as f:
    numbers = [row.rstrip() for row in f]
    numbers = list(map(int, numbers[0].split()))
    sum_numbers = reduce(lambda x, y: x + y, numbers)
    print(f"Сумма чисел в файле: {sum_numbers}")
