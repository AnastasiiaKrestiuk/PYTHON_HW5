# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = 2
b = 3

def power(a, b):
    if (a == 0 and b <= 0):
        print("Невозможно возвести 0 в степень меньше 1")
    if (a == 1 or a == 0): 
        return a
    if (b > 1):
        return a * power(a, b-1)
    if (b < 1):
        return 1 / a * power(a, b+1)
    return a

print(power(a, b))