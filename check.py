import math
x = float(input("x = "))
n = int(input("Количество шагов: "))
y = 1
step = 1
a = float
b = float
for i in a:
    a = a * (-x)
    i += 1
for i in b:
    b = b * i
    i += 1
while (step <= n):
    y += (-1) ** step * (a ** step/ b)
    step += 1
print(y)
