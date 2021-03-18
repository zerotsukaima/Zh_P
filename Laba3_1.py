s = input("Введите строку ")
if s[len(s) - 1] != ".":
    s = input("Введите строку ")
print(len(s))
for i in s:
    print(s[::])