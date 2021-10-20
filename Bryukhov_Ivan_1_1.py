duration = int(input('Введите число: '))
if duration <= 59:
    print(duration, 'секунд')
elif duration <= 3599:
    m = duration // 60
    s = duration % 60
    print(m, 'минут', s, 'секунд')
elif duration <= 86399:
    h = duration // 3600
    m = (duration - h * 3600) // 60
    s = duration % 60
    print(h, 'час', m, 'минут', s, 'секунд')
else:
    d = duration // 86400
    h = (duration - d * 86400) // 3600
    m = (duration - (d * 86400 + h * 3600)) // 60
    s = duration % 60
    print(d, 'дней', h, 'час', m, 'минут', s, 'секунд')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
