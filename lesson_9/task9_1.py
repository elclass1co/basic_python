# Создать класс TrafficLight (светофор):
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
from time import sleep
from colorama import Fore


class TrafficLight:
    __color = 'Red'

    def color_switch(self):
        print(f'{Fore.RED} {self.__color}')
        sleep(7)
        TrafficLight.__color = 'Yellow'
        print(f'{Fore.YELLOW} {self.__color}')
        sleep(2)
        TrafficLight.__color = 'Green'
        print(f'{Fore.GREEN} {self.__color}')


a = TrafficLight()
a.color_switch()

