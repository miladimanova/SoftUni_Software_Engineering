import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = (1 / 8) * break_duration
relax_time = (1 / 4) * break_duration
taken_time = lunch_time + relax_time
time_left = break_duration - taken_time

diff = math.ceil(abs(time_left - episode_duration))

if episode_duration <= time_left:
    print(f'You have enough time to watch {series_name} and left with {diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {diff} more minutes.")
