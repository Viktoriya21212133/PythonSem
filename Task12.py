# Задача 12: Петя и Катя – брат и сестра. Петя – студент,  а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

x = 10
y = 10
p = x*y
s = x+y
input_x = int(input("Try to guess the first number: "))
input_y = int(input("Try guessing the second number: "))
if x*y == input_x*input_y and x+y == input_x+input_y:
    print("Did you guess the numbers! Summ = ", input_x+input_y, ", work = ",input_y*input_x)
else: 
    print("Try again!")