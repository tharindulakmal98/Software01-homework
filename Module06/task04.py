def number(list):
    total = 0
    for i in list:
        total += i
    return total

my_list = [2,3,4,5,6]
result = number(my_list)
print("sum of the list is:", result)