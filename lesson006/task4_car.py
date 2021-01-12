# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    directions = {"left": "лево", "right": "право"}

    def __init__(self):
        self.speed = 0
        self.color = ""
        self.name = ""
        self.is_police = False
        self.__state = {"go": False, "action": []}


    def go(self, speed):
        if self.__state["go"]:
            print("Машина уже находится в движении")
            return False
        else:
            self.__state["go"] = True

        if speed < 1 or speed > 200:
            self.speed = 1
            print(f"Ты чего такой быстрый? Остынь до {self.speed} км/ч")
        else:
            self.speed = speed
            print(f"Вы разогнались до {self.speed} км/ч")
            
        self.__state["action"].append(f"Машина начала движение (со скоростью {self.speed} км/ч)")


    def stop(self):
        if not self.__state["go"]:
            print("Машина уже стоит")
            return False
        else:
            self.__state["go"] = False

        self.speed = 0
        print("Вы остановились")
        self.__state["action"].append("Машина остановилась")


    def turn(self, direction):
        if direction != "лево" and direction != "право":
            print("Неправильное направление движения.")
            return False
        if not self.__state["go"]:
            print("Машина стоит.")
            return False
        
        print(f"Вы повернули на{direction}")
        self.__state["action"].append(f"Машина  повернула на{direction}")


    def show_speed(self):
        print(f"Скорость машины: {self.speed} км/ч")

    def print_actions(self):
        print(f"Проделанные действия: {self.__state['action']}")


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color

    def show_speed(self):
        print(f"{'' if self.speed <= 60 else 'Вы превысили скорость на ' + str(self.speed - 60) + ' км/ч. '}Ваша скорость: {self.speed}")


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color

    def show_speed(self):
        print(f"{'' if self.speed <= 40 else 'Вы превысили скорость на ' + str(self.speed - 40) + ' км/ч. '}Ваша скорость: {self.speed}")

class PoliceCar(Car):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.color = "Бело-синия"
        self.is_police = True


police = PoliceCar("Жигуль")
sport = SportCar("Lamborgini", "Жёлтый")
work = WorkCar("Нива", "Коричневый")
town = TownCar("Honda", "Белая")


police.go(90)
police.turn(Car.directions["left"])
police.turn(Car.directions["right"])
police.show_speed()
police.stop()
police.print_actions()
print("-----------------------------")
sport.go(120)
sport.turn(Car.directions["left"])
sport.turn(Car.directions["right"])
sport.turn(Car.directions["right"])
sport.turn(Car.directions["left"])
sport.show_speed()
sport.stop()
sport.print_actions()
print("-----------------------------")
work.go(75)
work.turn(Car.directions["left"])
work.show_speed()
work.stop()
work.print_actions()
print("-----------------------------")
town.go(80)
town.turn(Car.directions["right"])
town.show_speed()
town.stop()
town.print_actions()