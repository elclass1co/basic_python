# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты(USD, EUR, ...)
#  и возвращающую курс этой валюты по отношению к рублю.Использовать библиотеку requests.
# В качестве API можно использовать http: // www.cbr.ru / scripts / XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере,
# посмотреть содержимое ответа.Можно ли, используя только методы класса str,
# решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None.Можно ли сделать работу функции не зависящей от того,
#  в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

from requests import get, utils


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
            a = float(cur[0].replace(",", "."))
            return a


content = parse()
currency = input('Введите код валюты: ').upper()

print(currency_rates(currency, content))
