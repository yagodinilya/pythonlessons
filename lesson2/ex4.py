string = input("Введите несколько слов с пробелами: ").split()
for i, a in enumerate(string, 1):
    print(i, a) if len(a) <= 10 else print(i, (a[:10]))