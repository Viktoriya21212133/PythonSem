# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fibonacci_numbers(n):
    if n in (1, 2):
        return 1
    return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)

num = int(input("Enter N-е number Fibonachi: "))
print("Result = ", fibonacci_numbers(num))