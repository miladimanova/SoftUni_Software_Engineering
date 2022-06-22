inherited_money = float(input())
up_to_year = int(input())
money_to_spend = 0
ivancho_age = 17
odd_year = 0
for year in range(1800, up_to_year + 1):
    if year % 2 == 0:
        ivancho_age += 1
        money_to_spend += 12000
    elif year % 2 != 0:
        ivancho_age += 1
        if ivancho_age % 2 != 0:
            money_to_spend += 12000 + 50 * (ivancho_age)

diff = abs(inherited_money - money_to_spend)
if inherited_money >= money_to_spend:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')