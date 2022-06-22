season = input()
km_per_month = float(input())

if 10000 < km_per_month <= 20000:
    price_per_km = 1.45
elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.95
    elif season == 'Summer':
        price_per_km = 1.10
    elif season == 'Winter':
        price_per_km = 1.25
elif km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.75
    elif season == 'Summer':
        price_per_km = 0.90
    elif season == 'Winter':
        price_per_km = 1.05
total_payment = km_per_month * price_per_km * 4
taxes = total_payment * 0.10
net_salary = total_payment - taxes
print(f'{net_salary:.2f}')