# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

# Представлен список чисел.Определить элементы списка, не имеющие повторений.
#  Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

# При увеличении списка множества дают существенный выигрыш во времени.
# Так если список будет содержать 10 ^ 3 элементов. Время выполнения будет:
# 9032 0.011662493999999999
# 9032 0.006560726999999999
# 33000 0.000455663000000002 Множества
# А если возьмем 10 ^ 4:
# 87632 1.159075563
# 87632 0.5588056029999999
# 524520 0.0030800039999998585
# Так же хотел проверить на 10^6, но не дождался выполнения программы. Ждал минут 15 :)

from sys import getsizeof
from time import perf_counter


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
result = [i for i in src if src.count(i) == 1]

print(result, getsizeof(result), perf_counter() - start)

start = perf_counter()

result = []
for el in src:
    if el not in result:
        result.append(el)
    else:
        result.remove(el)
print(result, getsizeof(result), perf_counter() - start)

start = perf_counter()
result = set()
tmp = set()
for el in src:
    if el not in tmp:
        result.add(el)
    else:
        result.discard(el)
    tmp.add(el)

print(result, getsizeof(result), perf_counter() - start)
