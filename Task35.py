# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

def if_simple(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print("Prime number")
    else:
        print("Number is not prime")

num = int(input('Enter number: '))
print(if_simple(num))