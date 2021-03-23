while True:
    hour = int(input("-> "))
    if 5 < hour < 10:
        print("Morning!")
    elif 10 <= hour < 17:
        print("Day!")
    elif 17 <= hour < 23:
        print("Evening!")
    elif 23 <= hour <= 24 or 0 <= hour <= 5:
        print("Night!")
    else:
        print("End.")
        break