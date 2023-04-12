# Задача №3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

a=int(input("Enter the number of students in the class №1 "))
b=int(input("Enter the number of students in the class №2 "))
c=int(input("Enter the number of students in the class №3 "))
print("Need to buy", a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2, "desks")