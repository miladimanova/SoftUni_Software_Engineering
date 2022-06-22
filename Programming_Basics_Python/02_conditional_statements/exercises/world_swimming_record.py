record = float(input())
distance = float(input())
time_per_meter = float(input())

delay = distance // 15 * 12.5

score_Ivan = distance * time_per_meter + delay
time_difference = abs(record - score_Ivan)

if score_Ivan < record:
    print(f'Yes, he succeeded! The new world record is {score_Ivan:.2f} seconds.')
else:
    print(f'No, he failed! He was {time_difference:.2f} seconds slower.')