# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


def odd_nums(num):
    odd_nums_gen = [num for num in range(1, num + 1, 2)]
    return odd_nums_gen


print(odd_nums(15))
