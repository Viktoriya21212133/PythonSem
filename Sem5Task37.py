# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

import random
num = int(input("Enter the value of the sequence of numbers: "))
new_list = [random.randint(0, 10) for i in range(num)]
# При помощи среза
print("Source List: ", new_list, "\n", "List in reverse order: ", new_list[:: -1])
# При помощи команты
new_list.reverse()
print("List in reverse order:", new_list)