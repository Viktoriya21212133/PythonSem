# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

N = abs(int(input("Enter the number of list items А: ")))
A_entered = input("Enter list elements separated by a space: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N:
    print('ERROR!')
else:
    X = int(input("Enter the number X to be found in the list: "))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
    print(f'Number {X} appears in the list A {count} once') 
    
    