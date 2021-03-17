import math
x = float(input("Vvedite znachecnie X "))
n = int(input("Vvedite chislo shagov "))
step = 1
y = 1.0
while step <= n:
    y += float((-1) ** step) * (x ** step) / math.factorial(step)
    step = step + 1
print(y)
