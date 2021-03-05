# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:

# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.

# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными

from random import choice


def get_jokes():
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    jokes_num = int(input("Введите кол-во шуток: "))
    repeat_flag = input(
        "Можно ли использовать одно слово в разных шутках? (Y/N): ")
    if repeat_flag == 'Y':
        for i in range(jokes_num):
            joke = [choice(nouns), choice(adverbs), choice(adjectives)]
            joke = " ".join(joke)
            jokes_list.append(joke)
    else:
        if jokes_num > 5:
            print('Невозможно создать столько шуток, введите число 5 или меньше')
        else:
            for i in range(jokes_num):
                a = choice(nouns)
                b = choice(adverbs)
                c = choice(adjectives)
                joke = [a, b, c]
                joke = " ".join(joke)
                jokes_list.append(joke)
                nouns.remove(a)
                adverbs.remove(b)
                adjectives.remove(c)
    return(jokes_list)


print(get_jokes())
