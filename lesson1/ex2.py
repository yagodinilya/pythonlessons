num = int(input("Введите кол-во секунд: "))

sec = num % 60
num = num - sec
hours = num // 3600
num = num - (hours * 3600)
min = num // 60

print(f"{hours:02d}:{min:02d}:{sec:02d}")
