# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5


def val_checker(num):
    if num < 0:
        raise ValueError(f"wrong val {num}")
    else:
        def decor(func):
            def wrapper(num):
                return func(num)
            return wrapper(num)


@val_checker
def calc_cub(num):
    return num ** 3


print(calc_cub(5))