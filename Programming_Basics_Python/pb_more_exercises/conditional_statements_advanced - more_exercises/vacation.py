budget = float(input())
season = input()

if budget <= 1000:
    place_to_stay = 'Camp'
    if season == 'Summer':
        destination = 'Alaska'
        vacation_price = budget * 0.65
    elif season == 'Winter':
        destination = 'Morocco'
        vacation_price = budget * 0.45
elif 1000 < budget <= 3000:
    place_to_stay = 'Hut'
    if season == 'Summer':
        destination = 'Alaska'
        vacation_price = budget * 0.80
    elif season == 'Winter':
        destination = 'Morocco'
        vacation_price = budget * 0.60
elif budget > 3000:
    place_to_stay = 'Hotel'
    vacation_price = budget * 0.90
    if season == 'Summer':
        destination = 'Alaska'
    elif season == 'Winter':
        destination = 'Morocco'
print(f'{destination} - {place_to_stay} - {vacation_price:.2f}')