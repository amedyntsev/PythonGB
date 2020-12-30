# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять"}
with open("task_4.txt", encoding="utf-8") as f:
    words = [row for row in f]

with open("task_4plus.txt", "w", encoding="utf-8") as f:
    f.writelines([row.replace(row.split()[0], dictionary.get(row.split()[0])) for row in words])
