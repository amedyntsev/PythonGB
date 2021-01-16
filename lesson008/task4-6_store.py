# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


from abc import ABC, abstractmethod


def is_digit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


class CapacityException(Exception):
    def __init__(self, txt):
        self.txt = txt


class EquipmentException(Exception):
    def __init__(self, txt):
        self.txt = txt


class CompanyEquipment:
    def __init__(self, name):
        self.__place_equip = {"prog_room": [], "clerk_room": [], "openspace": []}
        self.__name = name

    def add_equipment(self, equip):
        if type(equip) in (Printer, Scanner, Copier):
            key_list = list(self.__place_equip.keys())
            while True:
                print("1. Комната программистов\n2. Комната менеджеров\n3. Open space\n4. Отмена")
                select = input("Выберете пункт меню куда необходимо добавить оборудование (4 - для выхода): ")
                if select == "4":
                    break
                if not is_digit(select) or not int(select) in [1, 2, 3]:
                    continue
                self.__place_equip[key_list[int(select)]].append(equip)
                break
        else:
            raise EquipmentException("Исключение. В помещения добавляется только оргтехника (принтеры, сканеры, копиры)")

    def clear_equipment(self):
        self.__place_equip["prog_room"].clear()
        self.__place_equip["clerk_room"].clear()
        self.__place_equip["openspace"].clear()

    def __str__(self):
        info = f"Название компании: {self.__name}\n"
        info += f"Комната программистов (кол-во - {self.__place_equip['prog_room']}):\n"
        for element in self.__place_equip['prog_room']:
            info += f"{element}"
        info += f"Комната менеджеров (кол-во - {self.__place_equip['clerk_room']}):\n"
        for element in self.__place_equip['clerk_room']:
            info += f"{element}"
        info += f"Open space (кол-во - {self.__place_equip['openspace']}):\n"
        for element in self.__place_equip['openspace']:
            info += f"{element}"
        return f"+ Информация компании и о распределении оргтехники по комнатам +\n{info}"


class StorageEquipment:
    def __init__(self, capacity):
        if not is_digit(capacity) or capacity < 2:
            capacity = 2
        self.__equip_dict = {"printers": [], "scanners": [], "copiers": []}
        self.__capacity = capacity

    def check_capacity(self):
        if (sum([len(val) for val in self.__equip_dict.values()]) + 1) > self.__capacity:
            raise CapacityException(f"Исключение. Склад переполнен оргтехникой. Максимум: {self.__capacity}")

    def add_equipment(self, equip):
        if type(equip) in (Printer, Scanner, Copier):
            self.check_capacity()
            self.__equip_list.append(equip)
        else:
            raise EquipmentException("Исключение. На склад добавляется только оргтехника (принтеры, сканеры, копиры)")

    def clear_list_equipment(self):
        self.__equip_list.clear()


class Equipment(ABC):
    def __init__(self, name, serial, price):
        self.name = name
        self.serial = serial
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        pass


class Printer(Equipment):
    def __init__(self, name, serial, price):
        super().__init__(name, serial, price)

class Scanner(Equipment):
    pass


class Copier(Equipment):
    pass


while True:
    print(f"")
    pass
