n = int(input("Введите целое положительное число: "))
x = 10
max = n % x
while n % x < n:
    if (n % x) // (x / 10) > max:
        max = (n % x) // (x // 10)
        if max == 9:
            break
    x *= 10
print(max)
