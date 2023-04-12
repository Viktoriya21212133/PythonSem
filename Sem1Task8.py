# Задача 8. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 

m = int(input("Enter m: "))
n = int(input("Enter n: "))
k = int(input("How many slices to break off? "))

if k < m * n:
    if k % m == 0 or k % n == 0:
        print("Yes!")
    else:
        print("No :(")