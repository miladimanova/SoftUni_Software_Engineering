import math

days_cont = int(input())
left_food_kg = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

turtle_food_kg = turtle_food_per_day / 1000
total_need_food = (dog_food_per_day + cat_food_per_day + turtle_food_kg) * days_cont
diff = abs(left_food_kg - total_need_food)
if left_food_kg >= total_need_food:
    print(f'{math.floor(diff)} kilos of food left.')
else:
    print(f'{math.ceil(diff)} more kilos of food are needed.')