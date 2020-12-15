from random import randint
my_list = [randint(5, 30) for i in range(20)]
my_list_1 = [n for n in my_list if my_list.count(n) == 1]
print(f"Список чисел:\n {my_list}, \nСписок без повторений:\n {my_list_1}")

