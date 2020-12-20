string = input("Введите числа без пробелов: ").split()
for i in range(1, len(string), 2):
    string[i], string[i - 1] = string[i - 1], string[i]
    print(string)