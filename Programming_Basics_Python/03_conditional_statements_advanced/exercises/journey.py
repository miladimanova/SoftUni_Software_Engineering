budget = float(input())
season = input()
vacation_cost = 0

if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        vacation_cost = budget * 0.30
        print(f'Camp - {vacation_cost:.2f}')
    elif season == 'winter':
        vacation_cost = budget * 0.70
        print(f'Hotel - {vacation_cost:.2f}')
elif 100 < budget <= 1000:
    print('Somewhere in Balkans')
    if season == 'summer':
        vacation_cost = budget * 0.40
        print(f'Camp - {vacation_cost:.2f}')
    elif season == 'winter':
        vacation_cost = budget * 0.80
        print(f'Hotel - {vacation_cost:.2f}')
elif budget > 1000:
    print('Somewhere in Europe')
    vacation_cost = budget * 0.90
    print(f'Hotel - {vacation_cost:.2f}')