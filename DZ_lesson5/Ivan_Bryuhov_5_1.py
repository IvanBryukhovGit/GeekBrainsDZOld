# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def odd_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 1:
            yield i


odd_number = odd_numbers(15)
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))
