# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
# чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# ### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать,
# в каких ситуациях генератор даст эффект.

tutors1 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Петр', 'Сергей',
]
klasses1 = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def my_tuple(tutors, klasses):
    for i in range(len(tutors)):
        if len(klasses) < len(tutors) and i > len(klasses)-1:
           yield (tutors[i], None)
        else:
            yield (tutors[i], klasses[i])


my_yield = my_tuple(tutors1, klasses1)
print(next(my_yield))
print(next(my_yield))
print(next(my_yield))
print(next(my_yield))
print(next(my_yield))
print(next(my_yield))
print(next(my_yield))
print(next(my_yield))
print(next(my_yield))
