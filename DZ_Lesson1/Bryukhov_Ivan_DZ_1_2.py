# Создаем алгоритм для вычесления списка, состоящего из кубов нечётных чисел от 1 до 1000
cubeList = []
result_list = []
for oddNumbers in range(1,1001):
    if oddNumbers % 2 == 1:
        oddNumbers = oddNumbers ** 3
        cubeList.append(oddNumbers)
# Задание 1a: Создаем алгоритм для суммы чисел из списка, состоящего из кубов нечётных чисел от 1 до 1000
# Сумма цифр которох делится на 7 нацело

for num in cubeList:
    summ = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        summ += digit
    if summ % 7 == 0:
        result_list.append(summ)
        print(summ)
# Задание b и с: К каждому элемента списка доюавили 17 и заново выислили сумму исел из этого списка
# Условие добавлено и задания C* (Не создавая новый список)
# for num in cubeList:
#     summ = 0
#     num += 17
#     while num > 0:
#         digit = num % 10
#         num = num // 10
#         summ += digit
#     if summ % 7 == 0:
#         result_list.append(summ)
#         print(summ)
