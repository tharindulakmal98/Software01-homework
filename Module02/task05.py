talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

lots_total = (talents * 20 * 32) + (pounds * 32) + lots
grams_total = lots_total * 13.3

kg = int(grams_total // 1000)
g = grams_total % 1000

print(f"{kg} kilograms and {g:.2f} grams.")