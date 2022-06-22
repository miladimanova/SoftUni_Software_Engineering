import math
from math import floor

tournaments_count = int(input())
starting_points = int(input())
points = 0
number_of_winnings = 0
for _ in range(tournaments_count):
    tournament_stage = input()
    if tournament_stage == 'SF':
        points += 720
    elif tournament_stage == 'F':
        points += 1200
    elif tournament_stage == 'W':
        points += 2000
        number_of_winnings += 1

final_points = points + starting_points
average_points = points / tournaments_count

print(f'Final points: {final_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{number_of_winnings / tournaments_count * 100:.2f}%')




