destination = input()
enough_needed_money = False

while destination != 'End':
    trip_price = float(input())
    needed_money = 0

    while needed_money < trip_price:
        saved_amount = float(input())
        needed_money += saved_amount
    print(f'Going to {destination}!')
    destination = input()









