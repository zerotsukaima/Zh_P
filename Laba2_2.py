import math
from decimal import Decimal
x = float(input("Vvedite znachecnie X "))
n = int(input("Vvedite chislo shagov "))
step = 1
y = 1
while step <= n:
    y += ((-1) ** step) * (x ** step) / math.factorial(step)
    step = step + 1
print(y)
#завести отдельно переменную Числитель и потом применять ее в примере, чтобы Числитель вызывать и домножать на себя
#со знаменателем тоже самое, завести переменную Знаменатель и выполнять ее домножение
#в итоговой формуле будет y += Числитель/Знаменатель