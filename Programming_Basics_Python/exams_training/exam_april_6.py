locations_count = int(input())
for locations in range(1, locations_count + 1):
    expected_average_yield_per_day = float(input())
    days_digging_per_location = int(input())
    days_counter = 0
    gold_per_day = 0
    for days in range(1, days_digging_per_location + 1):
        extracted_gold = float(input())
        days_counter += 1
        gold_per_day += extracted_gold
        actual_average_yield_per_day = gold_per_day / days_counter
        diff = abs(expected_average_yield_per_day - actual_average_yield_per_day)
    if actual_average_yield_per_day >= expected_average_yield_per_day:
        print(f'Good job! Average gold per day: {actual_average_yield_per_day:.2f}.')
    else:
        print(f'You need {diff:.2f} gold.')


