numbers = []

while True:
    num = input("Please enter a number: ")

    if num == "":
        break

    numbers.append(float(num))

if numbers:
    numbers.sort(reverse=True)

    largest_five = numbers[:5]

    print("The greatest numbers in descending order:")

    for n in largest_five:
        print(f"{n:.1f}")
else:
    print("No numbers were entered.")