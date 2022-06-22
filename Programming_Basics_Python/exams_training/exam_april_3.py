month = input()
hours_in = int(input())
people_in_group = int(input())
time_of_the_day = input()

if month == 'march' or month == 'april' or month == 'may':
    if time_of_the_day == 'day':
        price_per_hour = 10.50
        if people_in_group >= 4:
            price_per_hour -= price_per_hour * 0.1
        if hours_in >= 5:
            price_per_hour -= price_per_hour * 0.5
    elif time_of_the_day == 'night':
        price_per_hour = 8.40
        if people_in_group >= 4:
            price_per_hour -= price_per_hour * 0.1
        if hours_in >= 5:
            price_per_hour -= price_per_hour * 0.5
elif month == 'june' or month == 'july' or month == 'august':
    if time_of_the_day == 'day':
        price_per_hour = 12.60
        if people_in_group >= 4:
            price_per_hour -= price_per_hour * 0.1
        if hours_in >= 5:
            price_per_hour -= price_per_hour * 0.5
    elif time_of_the_day == 'night':
        price_per_hour = 10.20
        if people_in_group >= 4:
            price_per_hour -= price_per_hour * 0.1
        if hours_in >= 5:
            price_per_hour -= price_per_hour * 0.5
total_cost_of_the_visit = price_per_hour * hours_in * people_in_group
print(f'Price per person for one hour: {price_per_hour:.2f}')
print(f'Total cost of the visit: {total_cost_of_the_visit:.2f}')

