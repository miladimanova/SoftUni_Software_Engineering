hours = int(input())
minutes = int(input())
total_time = (hours * 60) + minutes + 15
current_minutes = total_time % 60
current_hour = total_time // 60

if current_hour > 23:
    print(f'0:{current_minutes:02d}')
else:
    print(f'{current_hour}:{current_minutes:02d}')