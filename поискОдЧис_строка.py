while True:
    a = input("Введите трехзначное число: ")
    if a[0] == a[1] or a[1] == a[2] or a[2] == a[0]: #проверить если a[0]==a[1]==a[2]
        print("Есть одинаковые числа ")
    else:
        print("Нет одинаковых чисел ")