lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0

helmet_broken = lost_fights_count // 2 #шлем
sword_broken = lost_fights_count // 3 #меч
shield_broken = lost_fights_count // 6 #щит
armor_broken = lost_fights_count // 12 #броня

expenses = helmet_broken * helmet_price \
           + sword_broken * sword_price \
           + shield_broken * shield_price \
           + armor_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")