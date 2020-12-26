# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

user_sum = 0
def split_and_sum(string):
    result = {"local": 0, "message": ""}
    values = string.split()
    for element in values:
        if element.isdigit():
            element = float(element)
            result["local"] += element
        elif element == "exit":
            result["message"] = "exit"
            break
        else:
            continue
    return result
    

print("+ Сумма чисел +")
while True:
    print("——————————————————————————————————")
    string = input("Введите числа разделяя пробелом (для завершение введите exit): ")
    result = split_and_sum(string)
    user_sum += result["local"]
    print(f"Сумма чисел: {user_sum}")
    if result["message"] == "exit":
        break