"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для
 конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

name, hours, salary, bonus = argv
try:
    hours = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = hours * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')
