cats_count = int(input())
price_per_kg = 12.45
small_cats_food = 0
big_cats_food = 0
huge_cats_food = 0
small_cats_count = 0
big_cats_count = 0
huge_cats_count = 0
for cats in range(1, cats_count + 1):
    eaten_food = float(input())
    if 100 <= eaten_food < 200:
        small_cats_count += 1
        small_cats_food += eaten_food
    elif 200 <= eaten_food < 300:
        big_cats_count += 1
        big_cats_food += eaten_food
    elif 300 <= eaten_food < 400:
        huge_cats_count += 1
        huge_cats_food += eaten_food
total_eaten_food = small_cats_food + big_cats_food + huge_cats_food
price_per_day = total_eaten_food / 1000 * price_per_kg
print(f'Group 1: {small_cats_count} cats.')
print(f'Group 2: {big_cats_count} cats.')
print(f'Group 3: {huge_cats_count} cats.')
print(f'Price for food per day: {price_per_day:.2f} lv.')