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
    location = "Компания"

    def __init__(self, name_company):
        self.__place_equip = {"prog_room": [], "clerk_room": [], "openspace": []}
        self.__name_company = str(name_company)

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
                equip.location = CompanyEquipment.location
                self.__place_equip[key_list[int(select)]].append(equip)
                break
        else:
            raise EquipmentException("Исключение. В помещения добавляется только оргтехника (принтеры, сканеры, копиры)")

    def clear_equipment(self):
        self.__place_equip["prog_room"].clear()
        self.__place_equip["clerk_room"].clear()
        self.__place_equip["openspace"].clear()

    def __str__(self):
        info = f"Название компании: {self.__name_company}\n"
        info += f"Комната программистов (кол-во - {self.__place_equip['prog_room']}):\n"
        for element in self.__place_equip['prog_room']:
            info += f"{element}\n"
        info += f"Комната менеджеров (кол-во - {self.__place_equip['clerk_room']}):\n"
        for element in self.__place_equip['clerk_room']:
            info += f"{element}\n"
        info += f"Open space (кол-во - {self.__place_equip['openspace']}):\n"
        for element in self.__place_equip['openspace']:
            info += f"{element}\n"
        return f"+ Информация компании и о распределении оргтехники по комнатам +\n{info}"


class StorageEquipment:
    location = "Склад"
    full_count = 0

    def __init__(self, capacity=10):
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
            equip.location = StorageEquipment.location
            self.__equip_dict[equip.type_string()].append(equip)
            StorageEquipment.full_count += 1
        else:
            raise EquipmentException("Исключение. На склад добавляется только оргтехника (принтеры, сканеры, копиры)")

    def remove_equipment(self, equip):
        self.__equip_dict[equip.type_string()] = [el for el in self.__equip_dict[equip.type_string()] if el.id != equip.id]

    def get_equip_by_id(self, id):
        equip_obj = None
        for equip_type in self.__equip_dict:
            for equip in self.__equip_dict[equip_type]:
                if equip.id == id:
                    equip_obj = equip
                    break
            if equip_obj != None:
                break
        return equip_obj

    def clear_list_equipment(self):
        self.__equip_list.clear()

    def __str__(self):
        result = ""
        result += "+++++ Информация о складе +++++\n"
        result += f"Вместимость: {self.__capacity}\nЗанято: {StorageEquipment.full_count} из {self.__capacity}\n"
        for equip_type in self.__equip_dict:
            result += f"\n**********\n{equip_type}:\nКол-во – {len(self.__equip_dict[equip_type])}\nСписок →\n"
            for equip in self.__equip_dict[equip_type]:
                result += f"{equip.id} – {equip.name} ; "
        return result


class Equipment(ABC):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__id = StorageEquipment.full_count + 1

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(str(name)) < 6:
            raise EquipmentException("Исключение. В названии оборудования должно быть больше 6 символов")
        self.__name = name

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        if not location in ["Склад", "Компания"]:
            raise Exception
        self.__location = location

    @abstractmethod
    def type_string(self):
        pass


class Printer(Equipment):
    types = ["Матричный", "Струйный", "Лазерный"]

    def __init__(self, name, location="Склад", type_printer=0):
        super().__init__(name, location)
        self.type_printer = Printer.types[type_printer]

    @property
    def type_printer(self):
        return self.__type_printer

    @type_printer.setter
    def type_printer(self, type_printer):
        if not type_printer in Printer.types:
            raise EquipmentException(f"Исключение. Принтер можно выбрать только из этих трёх типов: {Printer.types}")
        self.__type_printer = type_printer

    def __str__(self):
        result = f"Принтер – {self.name}, {self.type_printer} ; "
        return result

    def type_string(self):
        return "printers"


class Scanner(Equipment):
    def __init__(self, name, location="Склад"):
        super().__init__(name, location)

    def __str__(self):
        result = f"Сканер – {self.name} ; "
        return result

    def type_string(self):
        return "scanners"


class Copier(Equipment):
    def __init__(self, name, location="Склад"):
        super().__init__(name, location)

    def __str__(self):
        result = f"Копир – {self.name} ; "
        return result

    def type_string(self):
        return "copiers"


company = None
storage = None
while True:
    if type(company) != CompanyEquipment:
        name_company = input("Введите название компании с которой будете работать (не менее 4-х символов): ")
        if len(name_company) < 4:
            continue
        company = CompanyEquipment(name_company)
    elif type(storage) != StorageEquipment:
        capacity_storage = input("Введите объём склада (целое положительное число не меньше 2): ")
        if not is_digit(capacity_storage):
            continue
        storage = StorageEquipment(int(capacity_storage))
    else:
        try:
            print(" ================================================== \n")
            print("1. Добавить оборудование\n2. Инфо о складе\n3. Перенести в компанию\n4. Инфо о компании\n5. Выход")
            select = input("Выберете пункт меню, что нужно сделать: ")
            if select == "5":
                break
            if not select in ["1", "2", "3", "4"]:
                continue
            if select == "1":
                while True:
                    print("Типы оборудования: 1-принтеры, 2-сканеры, 3-копиры")
                    type_equip = input("Выберете тип оборудования: ")
                    if not type_equip in ["1", "2", "3"]:
                        continue
                    name_equip = input("Введите название оборудования (не меньше 6 символов): ")
                    if len(name_equip) < 6:
                        continue
                    equip_obj = None
                    if type_equip == "1":
                        print(f"Типы принтеров: {[str(key + 1) + ' – ' + str(val) for key, val in enumerate(Printer.types)]}")
                        type_printer = input("Введите тип принтера (номер): ")
                        if not is_digit(type_printer) or not int(type_printer) in [1, 2, 3]:
                            continue
                        type_printer = int(type_printer) - 1
                        equip_obj = Printer(name_equip, storage.location, type_printer)
                        storage.add_equipment(equip_obj)
                    elif type_equip == "2":
                        equip_obj = Scanner(name_equip, storage.location)
                        storage.add_equipment(equip_obj)
                    else:
                        equip_obj = Copier(name_equip, storage.location)
                        storage.add_equipment(equip_obj)
                    break
            elif select == "2":
                print(storage)
            elif select == "3":
                equip_id = input("Введите id оборудования, которое необходимо перенести в компанию: ")
                if not is_digit(equip_id):
                    continue
                equip_obj = storage.get_equip_by_id(int(equip_id))
                if equip_obj == None:
                    print("Такого оборудования на складе нет")
                    continue
                storage.remove_equipment(equip_obj)
                company.add_equipment(equip_obj)
            else:
                print(company)
        except EquipmentException as ee:
            print(ee)
        except CapacityException as ce:
            print(ce)
        except Exception:
            print("Что-то пошло не так...")
