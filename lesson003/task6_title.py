# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, prcint(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# 65 - 

# Решение №1
def int_func(word):
    return word.title()

# Решение №2
def int_func2(word):
    if(ord(word[0]) > 96 or ord(word[0]) < 123):
        char = chr(ord(word[0]) - 32)
    else:
        char = word[0]
    return (char + word[1:len(word)])

print("——————————————————————————————————")
words = input("Введите строку слов: ").split()

result = ""
for word in words:
    result += int_func(word) + " "
print(f"Результат решение 1: {result}")

result = ""
for word in words:
    result += int_func2(word) + " "
print(f"Результат решение 2: {result}")