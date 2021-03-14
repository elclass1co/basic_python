# * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
#  которая передаётся в ответе сервера.Дата должна быть в виде объекта date.
#   Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?



from requests import get, utils
import datetime
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


def get_date(content):
    split_content = content[0].split('"')
    date = datetime.datetime.strptime(split_content[5], "%d.%m.%Y")
    print(date)




content = parse()
currency = input('Введите код валюты: ').upper()

print(currency_rates(currency, content))

get_date(content)