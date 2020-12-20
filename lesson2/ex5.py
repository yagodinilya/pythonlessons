my_list = [7, 5, 3, 3, 2]
number = int(input("Введите новый элемент рейтинга: "))
i = 0
for a in my_list:
    if number <= a:
        i += 1
my_list.insert(i, number)
print(my_list)
