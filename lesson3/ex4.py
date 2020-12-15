def my_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return "Введите положительное число и отрицательную степень"
    return result
print(my_func(5, -2))
