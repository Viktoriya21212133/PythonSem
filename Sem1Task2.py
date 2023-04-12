# Задача 2: Найдите сумму цифр трехзначного числа. 
n = int (input (' Enter nunber: '))
# Получаем первую цифру
number1 = n % 10
# Получаем вторую цифру
number2 = n % 100 // 10
# Получаем третью цифру
number3 = n // 100
result = number1 + number2 + number3
print ('The sum number = ', result)
