budget = float(input())
season = input()

if budget <= 100:
    classs = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        car_price = budget * 0.35
    elif season == 'Winter':
        car = 'Jeep'
        car_price = budget * 0.65

elif 100< budget <= 500:
    classs = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        car_price = budget * 0.45
    elif season == 'Winter':
        car = 'Jeep'
        car_price = budget * 0.80
elif budget > 500:
    classs = 'Luxury class'
    car = 'Jeep'
    car_price = budget * 0.90

print(classs)
print(f'{car} - {car_price:.2f}')