my_list = [2, 15, 22, 8, 10, 1, 5, 9]
my_list_1 = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(my_list_1)