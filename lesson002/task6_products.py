# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ 
# — характеристика товара, например название, а значение — список значений-характеристик, 
# например список названий товаров.

print("Для выхода из программы в любом месте введите 'exit'")
productId = 1
products = []
while True:
    name = input("Введите название товара: ")
    if name == "exit":
        break
    price = input("Введите цену за товар: ")
    if price == "exit":
        break
    count = input("Введите количество: ")
    if count == "exit":
        break
    unit = input("Введите единицу измерения (например, шт. или л.): ")
    if unit == "exit":
        break
    if not price.isdigit() or price == '' or not count.isdigit() or count == '':
        continue
    price = int(price)
    count = int(count)
    if price < 0 or count < 1:
        continue
    product = (productId, {"name": name, "price": price, "count": count, "unit": unit})
    products.append(product)
    productId += 1
    print("----------------------")

if len(products) > 0:
    print("--------------------------------------------")
    print("Введённые товары: ")
    for product in products:
        print(product)
    print("--------------------------------------------")
    print("Аналитика о товарах: ")
    keys = products[0][1].keys()
    result = {}
    for key in keys:
        result[key] = []
        for product in products:
            result[key].append(product[1].get(key))
        result[key] = list(set(result[key]))
    print(result)
