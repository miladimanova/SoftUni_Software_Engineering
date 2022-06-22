km_count = int(input())
time = input()
transportation_type = str
total_rice = 0
if time == 'day':
    if km_count < 20:
        transportation_type = 'Taxi'
        starting_tax = 0.70
        day_tariff_per_km = 0.79
        total_price = starting_tax + day_tariff_per_km * km_count
    elif 20 <= km_count < 100:
        transportation_type = "Bus"
        price_per_km = 0.09
        total_price = price_per_km * km_count
    elif km_count >= 100:
        transportation_type = 'Train'
        price_per_km = 0.06
        total_price = price_per_km * km_count
elif time == 'night':
    if km_count < 20:
        transportation_type = 'Taxi'
        starting_tax = 0.70
        night_tariff_per_km = 0.90
        total_price = starting_tax + night_tariff_per_km * km_count
    elif 20 <= km_count < 100:
        transportation_type = "Bus"
        price_per_km = 0.09
        total_price = price_per_km * km_count
    elif km_count >= 100:
        transportation_type = 'Train'
        price_per_km = 0.06
        total_price = price_per_km * km_count

print(f'{total_price:.2f}')
