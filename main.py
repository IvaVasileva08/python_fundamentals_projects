day = int(input())
hour_count = int(input())
price = 0
sum1 = 0
for j in range(1, day + 1):
    sum = 0
    for i in range(1, hour_count + 1):
        if i % 2 == 0 and j % 2 != 0:
                price = 1.25

        elif i % 2 != 0 and j % 2 == 0:
                price = 2.50

        else: price = 1
        sum += price
    print(f"Day: {j} – {sum:.2f} leva")
    sum1 += sum
print(f"Total: {sum1} leva")