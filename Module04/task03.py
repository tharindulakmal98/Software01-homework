numbers = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    number = float(user_input)
    numbers.append(number)

if numbers: 
    print(f"The smallest number entered is: {min(numbers)}")
    print(f"The largest number entered is: {max(numbers)}")

