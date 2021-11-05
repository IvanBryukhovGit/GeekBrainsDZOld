#Содаем функцию для склонения слова 'Секунд'
def my_time_sek (num):
    string = ''
    if num in range(10, 21):
        string = 'Секунд'
    elif num % 10 == 1:
        string = 'Секунда'
    elif num % 10 in range(2, 5):
        string = 'Секунды'
    else:
        string = 'Секунд'
    return string
#Содаем функцию для склонения слова 'Минут'
def my_time_min (num):
    string = ''
    if num in range(10, 21):
        string = 'Минут'
    elif num % 10 == 1:
        string = 'Минута'
    elif num % 10 in range(2, 5):
        string = 'Минуты'
    else:
        string = 'Минут'
    return string
#Содаем функцию для склонения слова 'Час'
def my_time_hour (num):
    string = ''
    if num in range(10, 21):
        string = 'Часов'
    elif num % 10 == 1:
        string = 'Час'
    elif num % 10 in range(2, 5):
        string = 'Часа'
    else:
        string = 'Часов'
    return string
#Содаем функцию для склонения слова 'День'
def my_time_day(num):
    string = ''
    if num in range(10, 21):
        string = 'Дней'
    elif num % 10 == 1:
        string = 'День'
    elif num % 10 in range(2, 5):
        string = 'Дня'
    else:
        string = 'Дней'
    return string
#Создаем алгоритм для реализации вывода информации в висимости от его продолжительности
duration = int(input('Введите число: '))
if duration <= 59:
    print(duration, my_time_sek(duration))
elif duration <= 3599:
    m = duration // 60
    s = duration % 60
    print(m, my_time_min(m), s, my_time_sek(s))
elif duration <= 86399:
    h = duration // 3600
    m = (duration - h * 3600) // 60
    s = duration % 60
    print(h, my_time_hour(h), m, my_time_min(m), s, my_time_sek(s))
else:
    d = duration // 86400
    h = (duration - d * 86400) // 3600
    m = (duration - (d * 86400 + h * 3600)) // 60
    s = duration % 60
    print(d, my_time_day(d), h, my_time_hour(h), m, my_time_min(m), s, my_time_sek(s))