#Определить время суток по заданному часу от 0 до 24.
#При неправильном значении (например, пользователь ввёл 75) нужно вывести сообщение об ошибке.
a = int(input("Введите время суток от 0 до 24: "))
if a > 24:
    print("Ошибка! ")
#распределить временные отрезки
if a >= 4 and a < 10:
    print("Утро")
elif a >= 10 and a < 16:
    print("День")
elif a >= 16 and a < 22:
    print("Вечер")
elif a >= 22 or a < 4: #исправила and на or
    print("Ночь")
