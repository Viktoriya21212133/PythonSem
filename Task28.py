# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

print("Enter two numbers: ") 
a = int(input())
b = int(input())
def sum_of_numbers(a, b):
    if b == 0:
        return a
    return sum_of_numbers(a+1, b-1) 
print(sum_of_numbers(a, b))