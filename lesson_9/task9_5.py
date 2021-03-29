# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    title = 'Pen'

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    title = 'Pen'

    def draw(self):
        print('Запуск отрисовки маркером')

p = Pen()
pncl = Pencil()
h = Handle()

p.draw()
pncl.draw()
h.draw()