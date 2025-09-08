def convo(gal):
    return gal * 3.785

while True:
    gasoline = float(input("Input volume of gasoline in gallons: "))
    if gasoline < 0:
        break
    result = convo(gasoline)
    print(result, "liters")
