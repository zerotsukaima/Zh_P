#пример задачи с удвоением каждого элемента в строке с конца строки, через индекс
str1 = input()
i = len(str1) - 1
while i >= 0:
    print(str1[i]*2, end="") # подходит для последнего задания
    i = i - 1
