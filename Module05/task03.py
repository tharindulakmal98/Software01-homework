user_input = int(input("Please enter an integer: "))

if user_input <= 1:
    print(f"{user_input} is not a prime number.")
else:
    for i in range(2, int(user_input ** 0.5) + 1):
        if user_input % i == 0:
            print(f"{user_input} is not a prime number.")
            break
    else:
        print(f"{user_input} is a prime number.")