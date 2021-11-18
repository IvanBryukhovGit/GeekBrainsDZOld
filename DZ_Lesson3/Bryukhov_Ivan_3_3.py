# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?
# name_list = ['Иван', 'Илья', 'Мария', 'Петр']

def thesaurus(*names):
    res = {}
    for name in names:
        key = name[0].upper()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res


print(thesaurus('Максим', 'Мария', 'Иван', 'Петр', 'Илья'))
