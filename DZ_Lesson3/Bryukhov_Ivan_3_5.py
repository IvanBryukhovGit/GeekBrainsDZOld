# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
humor = []
def get_jokes(n, flag = False):
    """ Функция создана для выборки случаных элементов из вышеуказанных списков;
    В последующем объединяняя эти элемнты в один список"""
    result = []
    for i in range(n):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        humors = f'{noun},{adverb},{adjective}'
        result.append(humors)
        my_list = []
        if flag == True:
            my_list = humors.split()
            for fun in nouns:
                for grein in my_list:
                    if fun == grein:
                        nouns.remove(fun)
            for blue in adverbs:
                for grein in my_list:
                    if blue == grein:
                        adverbs.remove(blue)
            for red in adjectives:
                for grein in my_list:
                    if red == grein:
                        adjectives.remove(red)
    return result


my_joke = get_jokes(3, True)
print(my_joke)

