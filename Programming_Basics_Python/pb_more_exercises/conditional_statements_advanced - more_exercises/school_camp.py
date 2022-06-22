season = input()
group_type = input()
students_count = int(input())
nights = int(input())

if season == 'Winter':
    if group_type == 'girls':
        price_per_night = 9.60
        sport = 'Gymnastics'
    elif group_type == 'boys':
        price_per_night = 9.60
        sport = 'Judo'
    elif group_type == 'mixed':
        price_per_night = 10
        sport = 'Ski'
elif season == 'Spring':
    if group_type == 'girls':
        price_per_night = 7.20
        sport = 'Athletics'
    elif group_type == 'boys':
        price_per_night = 7.20
        sport = 'Tennis'
    elif group_type == 'mixed':
        price_per_night = 9.50
        sport = 'Cycling'
elif season == 'Summer':
    if group_type == 'girls':
        price_per_night = 15
        sport = 'Volleyball'
    elif group_type == 'boys':
        price_per_night = 15
        sport = 'Football'
    elif group_type == 'mixed':
        price_per_night = 20
        sport = 'Swimming'
total_price_vacation = students_count * price_per_night * nights
if students_count >= 50:
    total_price_vacation -= total_price_vacation * 0.50
elif 20 <= students_count < 50:
    total_price_vacation -= total_price_vacation * 0.15
elif 10 <= students_count < 20:
    total_price_vacation -= total_price_vacation * 0.05
print(f'{sport} {total_price_vacation:.2f} lv.')