def number(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

my_list = [2, 3, 4, 5, 6]
mlist = number(my_list)
print("Original list:" , my_list)
print("cut-down list:", mlist)