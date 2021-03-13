# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...


def odd_nums(num):
    odd_nums_gen = (num for num in range(1, num + 1, 2))
    yield odd_nums_gen


a = odd_nums(15)

print(*next(a))
