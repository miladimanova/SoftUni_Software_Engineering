type_of_flowers = input()
count_of_flowers = int(input())
budget = int(input())
price_Roses = 5
price_Dahlias = 3.8
price_Tulips = 2.8
price_Narcissus = 3
price_Gladiolus = 2.5

if type_of_flowers == 'Roses':
    total_price = count_of_flowers * price_Roses
    if count_of_flowers > 80:
        total_price -= 0.10 * total_price
elif type_of_flowers == 'Dahlias':
    total_price = count_of_flowers * price_Dahlias
    if count_of_flowers > 90:
        total_price -= 0.15 * total_price
elif type_of_flowers == 'Tulips':
    total_price = count_of_flowers * price_Tulips
    if count_of_flowers > 80:
        total_price -= 0.15 * total_price
elif type_of_flowers == 'Narcissus':
    total_price = count_of_flowers * price_Narcissus
    if count_of_flowers < 120:
        total_price += 0.15 * total_price
elif type_of_flowers == 'Gladiolus':
    total_price = count_of_flowers * price_Gladiolus
    if count_of_flowers < 80:
        total_price += 0.20 * total_price
money_left = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {count_of_flowers} {type_of_flowers} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")