# Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
#
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ
# компьютера.

def parse():
    with open("nginx_log.txt", "r", encoding="utf-8") as logs:
        content = logs.readlines()
    ip_list = []
    request_type_list = []
    requested_resource_list = []
    parsed_tuples = []
    for i in content:
        i = i.rstrip().split('-')
        ip_list.append(i[0])
    for i in content:
        i = i.rstrip().split('"')
        i[1] = i[1].split(' ')
        request_type_list.append(i[1][0])
        requested_resource_list.append(i[1][1])
    for i in zip(ip_list, request_type_list, requested_resource_list):
        parsed_tuples.append(i)

    with open("ip_list.txt", "w", encoding="utf-8") as parsed_tuples_file:
        parsed_tuples_file.writelines(f'{parsed_tuples}')


if __name__ == "__main__":
    parse()
