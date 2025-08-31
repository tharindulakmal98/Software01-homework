correct_un = "tharindu98"
correct_pw = "Winteriscoming"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_un:
        if password == correct_pw:
            print("Welcome")
            break
        else:
            print("Incorrect password. Try again.")
    else:
        print("Incorrect username. Try again.")

    attempts += 1

if attempts == max_attempts:
    print("Access denied")