fuel_type = input()
liters_fuel = float(input())
discount_card = input()

if fuel_type == 'Diesel':
    total_price = liters_fuel * 2.33
    if discount_card == 'Yes':
        total_price = liters_fuel * (2.33 - 0.12)
    if 20 <= liters_fuel <= 25:
        total_price -= total_price * 0.08
    if liters_fuel > 25:
        total_price -= total_price * 0.10

elif fuel_type == 'Gasoline':
    total_price = liters_fuel * 2.22
    if discount_card == 'Yes':
        total_price = liters_fuel * (2.22 - 0.18)
    if 20 <= liters_fuel <= 25:
        total_price -= total_price * 0.08
    if liters_fuel > 25:
        total_price -= total_price * 0.10
elif fuel_type == 'Gas':
    total_price = liters_fuel * 0.93
    if discount_card == 'Yes':
        total_price = liters_fuel * (0.93 - 0.08)
    if 20 <= liters_fuel <= 25:
        total_price -= total_price * 0.08
    if liters_fuel > 25:
        total_price -= total_price * 0.10

print(f'{total_price:.2f} lv.')
