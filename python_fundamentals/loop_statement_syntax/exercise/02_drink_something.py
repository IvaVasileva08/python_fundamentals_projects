age = int(input())
type = ""

if age <= 14:
    type = "toddy"
elif age <= 18:
    type = "coke"
elif age <= 21:
    type = "beer"
elif age > 21:
    type = "whisky"
print(f"drink {type}")
