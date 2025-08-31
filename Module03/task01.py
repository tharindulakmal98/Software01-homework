length = int(input("Please enter the length of the zander (cm): "))

limit = 42

if length >= limit:
    print("The zander meets the size limit. keep it.")
else:
    difference = limit - length
    print("Release the fish back into the lake!")
    print(f"It is {difference} cm below the size limit.")