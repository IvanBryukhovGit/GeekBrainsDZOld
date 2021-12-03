# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при
# хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

import sys
import json

my_dict = dict()
with open('users.csv', 'r', encoding='utf-8') as a, \
        open('hobby.csv', 'r', encoding='utf-8') as b:
    for line in a:
        line2 = b.readline().strip()
        if not line2:
            line2 = None
        if line not in my_dict:
            line = my_dict[line.strip()] = line2
    content = b.read()
    if content:
        sys.exit(1)

with open('res.json', 'w', encoding='utf-8') as result:
    dict_string = json.dumps(my_dict, ensure_acii=False)
    result.write(dict_string)
with open('res.json', 'r', encoding='utf-8') as f:
    content = f.read()
    my_result = json.load(content)
print(my_result)
