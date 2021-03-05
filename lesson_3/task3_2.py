# * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
#  начинающимися с заглавной буквы.
#   Например:

# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# Проблема с заглавной буквой была решена, но возникла другая.
# Если ввести что - то, чего нет в словаре, вернется None, и не получится применить capitalize,
# программа сломается. Можно сделать обработчик ошибок, но его еще не проходили


def num_translate_adv(num):
    answer = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if answer.get(num) == None:
        num = num.lower()
        return(answer.get(num).capitalize())

    else:
        return(answer.get(num))


num = input('Введите число: ')

print(num_translate_adv(num))
