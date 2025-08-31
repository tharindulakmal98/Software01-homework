inches = float(input("Enter length in inches: "))

while inches >= 0:
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")
    print("Enter a negative value to quit")
    inches = float(input("Enter length in inches: "))