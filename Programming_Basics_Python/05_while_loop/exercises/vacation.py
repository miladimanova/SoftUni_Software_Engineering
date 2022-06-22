vacation_cost = float(input())
current_money = float(input())
spend_days_count = 0
days_count = 0
money_are_saved = True

while vacation_cost > current_money:
    action = input()
    amount = float(input())
    days_count += 1

    if action == "spend":
        spend_days_count += 1
        if current_money <= amount:
            current_money = 0
        else:
            current_money -= amount

        if spend_days_count == 5:
            money_are_saved = False
            break
    elif action == 'save':
        spend_days_count = 0
        current_money += amount

if money_are_saved:
    print(f'You saved the money for {days_count} days.')
else:
     print("You can't save the money.")
     print(days_count)