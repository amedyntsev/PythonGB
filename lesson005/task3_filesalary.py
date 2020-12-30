# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


with open("task_3.txt", "r", encoding="utf-8") as f:
    dict_employes = {row.split()[0]: float(row.split()[1]) for row in f}
    print(f"Средняя зарплата: {round(sum(dict_employes.values()) / len(dict_employes), 3)}")
    print(f"Сотрудники с зарплатой меньше 20000: {[e[0] for e in dict_employes.items() if e[1] < 20000]}")
