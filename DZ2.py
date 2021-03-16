import math
R1 = float(input("Введите R1 "))
R2 = float(input("Введите R2 при условии R1>R2 "))
S1 = (math.pi * (R1 ** 2))
S2 = (math.pi * (R2 ** 2))
S3 = (math.pi * ((R1 ** 2) - (R2 ** 2)))
print(S1)
print(S2)
print(S3)
