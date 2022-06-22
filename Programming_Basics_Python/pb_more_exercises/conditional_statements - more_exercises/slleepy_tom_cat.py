holidays_count = int(input())

play_time_norm = 30000
play_time_work_days = 63
play_time_off_days = 127
work_days = 365 - holidays_count

total_play_time_off_days = holidays_count * play_time_off_days
total_play_time_work_days = work_days * play_time_work_days
grand_total = total_play_time_work_days + total_play_time_off_days
diff = abs(grand_total - play_time_norm)
hours = diff // 60
minutes = diff % 60
if grand_total <= play_time_norm:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')