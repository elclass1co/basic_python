# 3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
#  задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.

percent = int(input("ВВедите кол-во процентов до 20: "))

if percent == 1:
    print(f'{percent} процент')

elif percent == 2 or percent == 3 or percent == 4:
    print(f'{percent} процента')


else:
    print(f'{percent} процентов')
