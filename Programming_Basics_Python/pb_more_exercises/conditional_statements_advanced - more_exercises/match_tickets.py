budget = float(input())
category = input()
number_of_people_in_group = int(input())
transportation_costs = 0

if category == 'VIP':
    ticket_price = 499.99
    if 1 <= number_of_people_in_group <= 4:
        transportation_costs = budget * 0.75
    elif 5 <= number_of_people_in_group <= 9:
        transportation_costs = budget * 0.60
    elif 10 <= number_of_people_in_group <= 24:
        transportation_costs = budget * 0.50
    elif 24 <= number_of_people_in_group <= 49:
        transportation_costs = budget * 0.40
    elif number_of_people_in_group >= 50:
        transportation_costs = budget * 0.25
elif category == 'Normal':
    ticket_price = 249.99
    if 1 <= number_of_people_in_group <= 4:
        transportation_costs = budget * 0.75
    elif 5 <= number_of_people_in_group <= 9:
        transportation_costs = budget * 0.60
    elif 10 <= number_of_people_in_group <= 24:
        transportation_costs = budget * 0.50
    elif 24 <= number_of_people_in_group <= 49:
        transportation_costs = budget * 0.40
    elif number_of_people_in_group >= 50:
        transportation_costs = budget * 0.25

money_left = budget - transportation_costs
total_tickets_cost = ticket_price * number_of_people_in_group
diff = abs(money_left - total_tickets_cost)
if money_left >= total_tickets_cost:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')

