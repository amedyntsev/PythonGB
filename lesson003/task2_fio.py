# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# def user_info(name, sname, year, city, email, phone):
def user_info(**kwargs):
    print(f"Имя: {kwargs['name']} ; Фамилия: {kwargs['sname']} ; " 
    + f"Год рождения: {kwargs['year']} ; Город: {kwargs['city']} ; " 
    + f"Email: {kwargs['email']} ; Телефон: {kwargs['phone']} ")


user_info(sname="Медынцев", name="Алексей", city="Москва", email="tesl@mail.ru", phone=12345, year=1991)