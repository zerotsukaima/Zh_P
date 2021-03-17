s = input("Введите фразу ")
while len(s) < 10:
    s = input("Vvedite frazu ")
else:
    print("Первые 4 символа", s[:4])
    print("Последние 4 символа", s[-4:])
    print('Символ посередине', s[len(s) // 2])
    print("Символы с 3-го по 8-й", s[2:8])

