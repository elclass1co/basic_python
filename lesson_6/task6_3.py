# Есть два файла: в одном хранятся ФИО пользователей сайта,
# а в другом — данные об их хобби. Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
#
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as u:
    users = u.readlines()
users_list = []
hobby_list = []
for i in users:
    i = i.rstrip().replace(",", " ")
    users_list.append(i)
with open('hobby.csv', 'r', encoding='utf-8') as h:
    hobby = h.readlines()
for i in hobby:
    i = i.rstrip()
    hobby_list.append(i)


user_hobby_dict = dict(zip_longest(users_list, hobby_list))

with open('users_hobby.csv', 'w', encoding='utf-8') as u_h:
    u_h.writelines(f'{user_hobby_dict}')

# print(users_list)
# print(hobby_list)
print(user_hobby_dict)
