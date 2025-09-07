user_city = []

for i in range(5):
    print("Please enter the name of a city: ", end="")
    city = input()
    user_city.append(city)

print("\n\nThe cities you entered:")

for city in user_city:
    print(city)