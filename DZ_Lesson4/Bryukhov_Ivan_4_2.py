# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно
# запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить п
# оставленную задачу? Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для
# работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в
# качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не
# зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
import requests

def currency_rates(val):
    browser = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    browser_code = browser.content.decode(encoding = browser.encoding)
    res = None
    if val not in browser_code:
        return res
    else:
        for el_1 in browser_code.split(f'{val}')[1:]:
            for el_2 in el_1.split('</Value')[:1]:
                res = round(float(el_2.split('<Value>')[1].replace(',', '.')), 2)
                return f'Курс валюты: {res} руб.'


if __name__ == '__main__':


    val_1 = input(str('Введите код валюты: '))
    print(currency_rates(val_1))
