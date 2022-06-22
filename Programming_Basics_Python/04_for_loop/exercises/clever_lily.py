from math import floor

age_Lily = int(input())
washing_machine_price = float(input())
price_per_one_toy = int(input())
money_price = 0
toys = 0
for year in range(1, age_Lily + 1):
    if year % 2 == 0:
        money_price += 10 * (year / 2)
    else:
        toys += 1
brother_takings = floor(age_Lily / 2)
savings = money_price + toys * price_per_one_toy - brother_takings
diff = abs(savings - washing_machine_price)
if savings >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
