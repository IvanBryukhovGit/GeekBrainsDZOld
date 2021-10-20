Duration = int(input('Введите число: '))
if Duration <= 59:
    print(Duration, 'секунд')
elif Duration <= 3599:
    m = Duration // 60;
    s = Duration % 60;
    print(m, 'минут', s, 'секунд')
elif Duration <= 86399:
    h = Duration // 3600;
    m = (Duration - h * 3600) // 60;
    s = Duration % 60;
    print(h, 'час', m, 'минут', s, 'секунд')
else:
    d = Duration // 86400;
    h = (Duration - d * 86400) // 3600;
    m = (Duration - (d * 86400 + h * 3600)) // 60;
    s = Duration % 60;
    print(d, 'дней', h, 'час', m, 'минут', s, 'секунд')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
