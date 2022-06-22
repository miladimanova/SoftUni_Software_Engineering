bought_food_kg = int(input())
total_eaten_food = 0
puppy_is_not_adopted = True
while puppy_is_not_adopted:
    eaten_food_gr_per_meal = input()
    if eaten_food_gr_per_meal == 'Adopted':
        puppy_is_not_adopted = False
        break
    else:
        total_eaten_food += int(eaten_food_gr_per_meal)
bought_food_gr = bought_food_kg * 1000
diff = abs(bought_food_gr - total_eaten_food)
if total_eaten_food <= bought_food_gr:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')
