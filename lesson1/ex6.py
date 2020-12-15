a = int(input("Введите ваш результат в км: "))
b = int(input("Введите желаемый результат в км: "))
c = 10
day = 1
c = c / 100

while a <= b:
    a = a + (a * c)
    day += 1
    print(f"На {day} день - {a:.2f} км")
if a > b:
    print(f"Вы пробежите {b} км на {day} день тренировок")