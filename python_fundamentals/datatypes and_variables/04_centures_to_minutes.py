centure = int(input())
year = centure * 100
day = int(year * 365.2422)
hour = day * 24
minute = int(hour * 60)
print(f"{centure} centuries = {year} years = {day} days = {hour} hours = {minute} minutes")