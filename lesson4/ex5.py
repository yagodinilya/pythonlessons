from functools import reduce

def my_list(i_1, i_2):
    return i_1 * i_2

my_list_1 = [i for i in range(100, 1001, 2)]
print(f"Список чисел: {my_list_1}\n Произведение чисел: {reduce(my_list, my_list_1)}")