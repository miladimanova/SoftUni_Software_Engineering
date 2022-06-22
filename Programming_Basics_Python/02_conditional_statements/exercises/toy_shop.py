trip_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_count_of_ordered_toys = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

total_order_amount = puzzles_count * puzzle_price + talking_dolls_count * talking_doll_price + teddy_bears_count * \
                     teddy_bear_price + minions_count * minion_price + trucks_count * truck_price

if total_count_of_ordered_toys >= 50:
    total_order_amount -= 0.25 * total_order_amount

rent = total_order_amount * 0.10
profit = total_order_amount - rent
difference = abs(profit - trip_price)

if trip_price <= profit:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')

