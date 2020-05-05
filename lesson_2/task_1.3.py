"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц 
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
MONTH = int(input('Введите номер месяца: '))
SEASONS_LIST = ['Зима', 'Весна', 'Лето', 'Осень']
if MONTH < 3:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_LIST[0]}')
elif MONTH > 2 and MONTH < 6:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_LIST[1]}')
elif MONTH > 5 and MONTH < 9:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_LIST[2]}')
elif MONTH > 8 and MONTH < 12:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_LIST[3]}')
elif MONTH > 12:
    print('Такого месяца не существует')
else:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_LIST[0]}')


SEASONS_DICT = {
    1: 'Зима',
    2: 'Весна',
    3: 'Лето',
    4: 'Осень'
}

if MONTH < 3:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_DICT[1]}')
elif MONTH > 2 and MONTH < 6:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_DICT[2]}')
elif MONTH > 5 and MONTH < 9:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_DICT[3]}')
elif MONTH > 8 and MONTH < 12:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_DICT[4]}')
elif MONTH > 12:
    print('Такого месяца не существует')
else:
    print(f'Месяцу под номером {MONTH} соотвествует сезон {SEASONS_DICT[1]}')
