import random

num_dice = int(input("How many dice to roll? : "))

sum_of_dice = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    sum_of_dice += roll

print(f"Sum of dice: {sum_of_dice}")