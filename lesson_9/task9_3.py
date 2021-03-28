# Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
#


class Worker:
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'Engineer'
    _income = {'wage': 3000, 'bonus': 5000}
    income = _income


class Position(Worker):

    def get_full_name(self):
        return f'{Worker.name} {Worker.surname}'

    def get_full_income(self):
        return f'{Worker.income.get("wage") + Worker.income.get("bonus")}'


p = Position()

print(p.get_full_name())
print(p.get_full_income())