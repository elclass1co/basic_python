# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
#  Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
#  Убедиться, что ничего лишнего не происходит.

from requests import get, utils
from sys import argv



def parse():
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings).split("Valute")
    return content


def currency_rates(currency, parse_data):
    for i in content:
        if currency in i:
            i = i.split(">")
            cur = i[-2].split("<")   # делим строку еще раз, получая число
            a = float(cur[0].replace(",", "."))   # преобразуем строку к числовому типу данных
            return a


content = parse()

if __name__ == "__main__":
    word = argv[1]
    print(currency_rates(word, content))




