exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

time_of_exam = exam_hour * 60 + exam_minutes
time_of_arrival = arrival_hour * 60 + arrival_minutes
diff = abs(time_of_exam - time_of_arrival)

if time_of_arrival == time_of_exam:
    print('On time')
elif time_of_arrival > time_of_exam:
    print('Late')
    hour = diff // 60
    minutes = diff % 60
    if diff > 59:
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f'{minutes} minutes after the start')

elif time_of_arrival < time_of_exam:
    if diff <= 30:
        print('On time')
        print(f'{diff} minutes before the start')
    else:
        print('Early')
        hour = diff // 60
        minutes = diff % 60
        if diff > 59:
            print(f'{hour}:{minutes:02d} hours before the start')
        else:
            print(f'{minutes} minutes before the start')
