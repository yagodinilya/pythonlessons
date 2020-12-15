from itertools import count, cycle
print("Для генерации нажмите Enter, для выхода нажмите 'q'")
for i in count(int(input("Введите число:"))):
    print(i, end=" ")
    quit = input()
    if quit == "q":
        break