profit = int(input("Введите вашу вырочку: "))
damages = int(input("Введите ваши издержки:"))
if profit > damages:
    profitability = profit - damages
    print(f"У вас прибыльная фирма, прибыль составляет: {profitability} рублей")
    emp = int(input("Введите кол-во сотрудников: "))
    emp = profitability // emp
    print(f"Прибыль на каждого сотрудника составляет: {emp} рублей")
else:
    print("Ваша фирма убыточная")
