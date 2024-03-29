# Создать вручную список, содержащий цены на товары(10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#  A) Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде < r > руб < kk > коп
# (например «5 руб 0 4 коп»).
#   Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек(должно быть 0 7 коп
#    или 00 коп).
# b) Вывести цены, отсортированные по возрастанию, новый список не создавать(доказать, что объект списка после сортировки остался тот же).
# C) Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# D)Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


price = [4.30, 5, 3, 2.08, 6.65, 9, 1.50, 7.34, 8.80, 10]


# b) Вывести цены, отсортированные по возрастанию, новый список не создавать(доказать, что объект списка после сортировки остался тот же).

print(id(price))
price.sort()
print(id(price))
print(price)

# C) Создать новый список, содержащий те же цены, но отсортированные по убыванию.


b = sorted(price, reverse=True)
print(b)

# D)Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


b = sorted(price)
print(f"{sorted(b[:len(b) - 6: -1])}")
