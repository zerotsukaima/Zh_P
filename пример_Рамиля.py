str_1 = input('Введите строку: ')

while str_1[-1] != '.':
    str_1 = input('Введите строку: ')

sum_1 = 1
sum_2 = 0

min = 300
max = 0

for i in str_1:
    if i == ' ':
        sum_1 += 1

for i in str_1:
    if i != ' ' and i != '.':
        sum_2 += 1
        continue
    if sum_2 > max:
        max = sum_2
    if sum_2 < min:
        min = sum_2
    sum_2 = 0

print('Длина строки: ' + str(len(str_1)) + ' символов.')
print('Количество слов: ' + str(sum_1) + '.')
print('Самое кортокое слов состоит из ' + str(min) + ' букв.')
print('Самое длинное слов состоит из ' + str(max) + ' букв.')

for i in str_1:
    if i != '*':
        print(i * 2, end='')