# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("task_2.txt", "r", encoding="utf-8") as f:
    info = [f'{row}. {value[:-1]} - {len(value.split())} слов' for row, value in enumerate(f, 1)]
    for element in info:
        print(element)
print(f"Всего строк: {len(info)}")
