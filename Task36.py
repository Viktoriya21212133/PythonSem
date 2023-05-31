# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows=6, num_columns=6):
    # создаем заголовок таблицы
    header = "  |"
    for i in range(1, num_columns+1):
        header += f" {i} "
    print(header)
    print("--+" + "---"*num_columns)
    # заполняем таблицу
    for i in range(1, num_rows+1):
        row = f"{i} |"
        for j in range(1, num_columns+1):
            row += f" {operation(i, j)} "
        print(row)

# пример использования функции с операцией умножения
def multiply(x, y):
    return x*y

print_operation_table(multiply)