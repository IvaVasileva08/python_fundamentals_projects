from math import ceil
number_of_people = int(input())
capacity = int(input())
total = ceil(number_of_people / capacity)
print(total)