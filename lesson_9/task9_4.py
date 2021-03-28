# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
from random import choice


class Car:
    turn_side = ['налево', 'направо']
    speed = 50
    color = 'Black'
    name = 'Toyota'
    is_police = False

    def go(self):
        print('Поехали')

    def stop(self):
        print('Остановились')

    def turn(self):
        print(f'Повернули {choice(self.turn_side)}')

    def show_speed(self):
        print(self.speed)



class TownCar(Car):
    speed = 70
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print(f'Моя скорость {self.speed}, мы не превышаем')


class SportCar(Car):
    pass


class WorkCar(Car):
    speed = 30

    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        else:
            print(f'Моя скорость {self.speed}, мы не превышаем')


class PoliceCar(Car):
    pass


c = Car()
tc = TownCar()
wc = WorkCar()

tc.show_speed()
tc.turn()
wc.show_speed()
wc.turn()
