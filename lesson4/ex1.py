from sys import argv
def pay():
    try:
        time, production, bonus = map(float, argv[1:])
        print(f"Зарплата: {time * production + bonus}")
    except ValueError:
        print(f"Введите корректные значения!")
pay()
