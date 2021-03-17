s = input("Vvedite stroku simvolov ")
while len(s) < 10:
    s = input("Vvedite stroku bolee 10 simvolov ")
else:
    print(s[:4])
    print(s[-4:])
if len(s) % 2 == 0:
    print(s[len(s) // 2 - 1] + s[len(s) // 2])
else:
    print(s[len(s) // 2])

