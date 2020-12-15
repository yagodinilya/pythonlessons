def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        number = s_1 / s_2
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return round(number, 2)
print(div(input("Введите первое число: "), input("Введите второе число: ")))
