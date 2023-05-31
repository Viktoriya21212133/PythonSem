# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n_coins = int(input("Enter number of coins on the table: ")) 
what_side = [random.randint(0, 1) for i in range(n_coins)] # условно обозначаем 0 - орлом, а 1 - решкой, и произвольно "рассыпаем их"
print(what_side)
orel = 0 # перевернуть количество орлов, чтобы все стали решками
reshka = 0 # перевернуть количество решек, чтобы все стали орлами
for i in range(len(what_side)):
    if what_side[i] == 0:
        orel += 1
    elif what_side[i] == 1:
        reshka += 1
print("You need to flip ", min(orel,reshka), " coins")