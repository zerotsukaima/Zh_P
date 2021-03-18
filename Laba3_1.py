s = input("Введите строку ")
if s[len(s) - 1] != ".":
    s = input("Введите строку с точкой ")
print(len(s))
p = 0
l = 0
for i in s:
    if i == " ":
        p = p + 1
    l = p + 1
print(l)
#print('i=', i)

count = 0
max = 0
min = 3000
for i in s:
    print('i=', i)
    print(s)
    if i == '.':
        count = count - 1
    if i != ' ':
        count = count + 1
        print("count=", count)
    else:
        count = 0 #ошибка тут
    if count > max:
        max = count
        print('max=', max)
    if count > 0: # и тут
        min = count
        print('min=', min)
print('max=', max)
print('min=', min)