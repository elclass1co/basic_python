# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным
# файла логов из предыдущего задания.
#
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.
#
def spam():
    with open("nginx_log.txt", "r", encoding="utf-8") as logs:
        content = logs.readlines()
    ip_list = []
    for i in content:
        i = i.rstrip().split('-')
        ip_list.append(i[0])

    most_common = None
    qty_most_common = 0
    ip_list_set = set(ip_list)
    for item in ip_list_set:
        qty = ip_list.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item

    print(most_common, qty_most_common)


spam()
