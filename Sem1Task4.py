# Задача 4. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
NumberCranes = int(input("Enter the number of cranes: "))
if NumberCranes % 6 == 0:
    x = NumberCranes//6
    a = 4*x
    print("Katya did", a, "cranes, а Petya and Serega by", x, "cranes")
else:
    print("ERROR")
