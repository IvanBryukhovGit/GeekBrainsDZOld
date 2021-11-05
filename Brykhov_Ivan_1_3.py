numbers = range(0, 21)
for num in numbers:
    if num in range(10, 21):
        print(num, 'Процентов')
    elif num % 10 == 1:
        print(num, 'Процент')
    elif num % 10 in range(2, 5):
        print(num, 'Процента')
    else:
        print(num, 'Процентов')



