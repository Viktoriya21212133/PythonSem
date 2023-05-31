n = int(input("List size: "))
n_digits = [int(input("Enter numbers: ")) for i in range(n)]
print(n_digits)
n_digits = set(n_digits)
print(n_digits)
print(len(n_digits))