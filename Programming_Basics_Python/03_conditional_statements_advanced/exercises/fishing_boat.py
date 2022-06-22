budget_group = int(input())
season = input()
count_of_fishman = int(input())
ship_rent = 0

if season == 'Spring':
    ship_rent = 3000
elif season == 'Autumn' or season == 'Summer':
    ship_rent = 4200
elif season == 'Winter':
    ship_rent = 2600

if count_of_fishman <= 6:
    ship_rent -= ship_rent * 0.10
elif 7 <= count_of_fishman <= 11:
    ship_rent -= ship_rent * 0.15
elif count_of_fishman >= 12:
    ship_rent -= ship_rent * 0.25

if season != 'Autumn' and count_of_fishman % 2 == 0:
    ship_rent -= ship_rent * 0.05

money_left = abs(budget_group - ship_rent)

if budget_group >= ship_rent:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')
