x = float(input("Введите значение X "))
n = int(input("Введите число шагов "))
y = 1
a = 0
b = 1
# шаг1: числитель и q его степень
q = (n - (n - 1))
if n == 0:
    x = 1
elif n == 1:
   x = x
while n >= 2:
    a = x * (x ** q)
    q = q + 1
    n = n - 1
print("Chislitel", a)
# шаг2: знаменатель не верно считает факториал сейчас
for i in range(2, n + 1):
    #print("Номер шага", i)
    b = b * i
print('factorial', b)
# шаг3: весь пример
step = n
while step >= n: # пока шаг больше или равен числу шагов от юзера, то решает
    y += ((-1) ** step) * (a / b)
    step = step - 1 #каждый раз уменьшая шаг
print(y)