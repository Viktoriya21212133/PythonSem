# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные

import random
n = int(input("Enter the number of Vasily's ratings in the journal: "))
grades_vas = [random.randint(1, 5) for i in range(n)]
print(grades_vas)

def replace_grades(grades):
    for i in range(len(grades)):
        if grades[i] > 3:
            grades[i] = 1
    return grades

grades_vas = replace_grades(grades_vas)
print(grades_vas)