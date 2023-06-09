# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

a = 2
b = 3

def sum(a, b):
    if (a < 0 or b < 0):
        print("Числа не должны быть отрицательными")
    if (b == 0):
        return a
    if(a == 0):
        return b
    c = sum(a-1, b)
    return c+1

print(sum(a, b))