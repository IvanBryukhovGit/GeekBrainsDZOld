cubeList = []
result_list = []
for oddNumbers in range(1,1001):
    if oddNumbers % 2 == 1:
        oddNumbers = oddNumbers ** 3
        cubeList.append(oddNumbers)
#Задача под a
for num in cubeList:
    summ = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        summ += digit
    if summ % 7 == 0:
        result_list.append(summ)
        print(summ)
#Задача b
# for num in cubeList:
#     summ = 0
#     num += 17 #Условие добавлено и задания C
#     while num > 0:
#         digit = num % 10
#         num = num // 10
#         summ += digit
#     if summ % 7 == 0:
#         result_list.append(summ)
#         print(summ)
