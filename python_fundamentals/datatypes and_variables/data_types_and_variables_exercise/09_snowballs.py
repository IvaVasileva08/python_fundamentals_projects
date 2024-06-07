number_of_snowballs = int(input())
max_calculate = 0
max_weight = 0
max_time = 0
max_quality = 0

for i in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    calculate = (weight / time) ** quality
    if calculate > max_calculate:
        max_calculate = calculate
        max_weight = weight
        max_time = time
        max_quality = quality

print(f"{max_weight} : {max_time} = {int(max_calculate)} ({max_quality})")