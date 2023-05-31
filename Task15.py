# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

import random

n_fruits = int(input("Enter number of watermelons: "))
weight = [] 
for i in range(n_fruits): 
    temp = random.randint(1, 15)
    weight.append(temp)
print(weight)
# min_weight = weight[0]
# max_weight = weight[0]
# for i in weight:
#     if i < min_weight:
#         min_weight = i
#     if i > max_weight:
#         max_weight = i
# print(max_weight, min_weight)
print(min(weight),max(weight)) #автоматический поиск мин и макс
print(sum(weight)) #сумма чисел в списке