n = int(input())
tank_capacity = 255
for i in range(n):
    liter_of_water = int(input())
    if liter_of_water > tank_capacity:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liter_of_water
count = 255 - tank_capacity
print(count)