# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
# и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    args = list(args)
    maxsum = 0
    pointer = 0
    while pointer < 2:
        pointer += 1
        maxsum += max(args)
        args.pop(args.index(max(args)))
    return maxsum

# Пример
print(my_func(99,15,32))
