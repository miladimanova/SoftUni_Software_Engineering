hrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()
total_count_flowers = hrysanthemums_count + tulips_count + roses_count
arrangement_price = 2
price_bouquet = 0
if season == 'Spring':
    hrysanthemums_price = 2
    roses_price = 4.10
    tulips_price = 2.50
    if holiday == 'Y':
        hrysanthemums_price += 2 * 0.15
        roses_price += 4.10 * 0.15
        tulips_price += 2.50 * 0.15
    price_bouquet = hrysanthemums_price * hrysanthemums_count + roses_price * roses_count + tulips_price * tulips_count
    if tulips_count > 7:
        price_bouquet -= price_bouquet * 0.05
    if total_count_flowers > 20:
        price_bouquet -= price_bouquet * 0.20
elif season == 'Summer':
    hrysanthemums_price = 2
    roses_price = 4.10
    tulips_price = 2.50
    if holiday == 'Y':
        hrysanthemums_price += 2 * 0.15
        roses_price += 4.10 * 0.15
        tulips_price += 2.50 * 0.15
    price_bouquet = hrysanthemums_price * hrysanthemums_count + roses_price * roses_count + tulips_price * tulips_count
    if total_count_flowers > 20:
        price_bouquet -= price_bouquet * 0.20
elif season == 'Autumn':
    hrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
    price_bouquet = hrysanthemums_price * hrysanthemums_count + roses_price * roses_count + tulips_price * tulips_count
    if holiday == 'Y':
        price_bouquet += price_bouquet * 0.15
    if total_count_flowers > 20:
        price_bouquet -= price_bouquet * 0.20
elif season == 'Winter':
    hrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
    if holiday == 'Y':
        hrysanthemums_price += 3.75 * 0.15
        roses_price += 4.50 * 0.15
        tulips_price += 4.15 * 0.15
    price_bouquet = hrysanthemums_price * hrysanthemums_count + roses_price * roses_count + tulips_price * tulips_count
    if roses_count >= 10:
        price_bouquet -= price_bouquet * 0.10
    if total_count_flowers > 20:
        price_bouquet -= price_bouquet * 0.20
print(f'{(price_bouquet + arrangement_price):.2f}')
