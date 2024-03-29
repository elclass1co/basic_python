# 6. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для
# вывода на экран записанных данных. При записи передавать из командной строки значение
# суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
#
# просто запуск скрипта — выводить все записи; запуск скрипта с одним параметром-числом — выводить все записи с
# номера, равного этому числу, до конца; запуск скрипта с двумя числами — выводить записи, начиная с номера,
# равного первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.

from sys import argv


def value_write(value):
    with open("bakery.csv", "a", encoding="utf-8") as bakery_file:
        bakery_file.write(value)


def value_print():
    with open("bakery.csv", "r", encoding="utf-8") as bakery_file:
        a = bakery_file.read()
    print(a)


def value_slice_print(val1, val2):
    with open("bakery.csv", "r", encoding="utf-8") as bakery_file:
        a = bakery_file.readlines()
    for i in range(val1 - 1, val2):
        print(a[i], end="")


value1 = argv[1] + "\n"
val1 = int(argv[1])
val2 = int(argv[2])


if __name__ == "__main__":
    if len(argv) == 3:
        value_slice_print(val1, val2)
    elif len(argv) == 2:
        value_write(value1)
    else:
        value_print()
