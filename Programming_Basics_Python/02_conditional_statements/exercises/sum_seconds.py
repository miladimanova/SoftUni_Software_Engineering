time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    total_time = f'{minutes}:0{seconds}'
    print(total_time)
else:
    total_time = f'{minutes}:{seconds}'
    print(total_time)