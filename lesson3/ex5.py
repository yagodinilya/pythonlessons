def my_func():
    x = 0
    while True:
        my_list = input("Введите числа:").split()
        for num in my_list:
            if num == "q":
                return x
            else:
                try:
                    x += int(num)
                except ValueError:
                    print(f"Для выхода из программы нажмите q")
        print(f"Сумма чисел = {x}")

my_func()
print(my_func())
