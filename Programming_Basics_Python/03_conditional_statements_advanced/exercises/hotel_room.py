    month = input()
nights_count = int(input())
price_per_night_studio = 0
price_per_night_apartment = 0

if month == 'May' or month == 'October':
    if 7 < nights_count <= 14:
        price_per_night_studio = 50 - (50 * 0.05)
        price_per_night_apartment = 65
    elif nights_count > 14:
        price_per_night_studio = 50 - (50 * 0.30)
        price_per_night_apartment = 65 - (65 * 0.10)
    else:
        price_per_night_studio = 50
        price_per_night_apartment = 65

elif month == 'June' or month == 'September':
    if nights_count > 14:
        price_per_night_studio = 75.2 - (75.2 * 0.20)
        price_per_night_apartment = 68.7 - (68.7 * 0.10)
    else:
        price_per_night_studio = 75.2
        price_per_night_apartment = 68.7
elif month == 'July' or month == 'August':
    if nights_count > 14:
        price_per_night_apartment = 77 - (77 * 0.10)
        price_per_night_studio = 76
    else:
        price_per_night_studio = 76
        price_per_night_apartment = 77

total_amount_studio = nights_count * price_per_night_studio
total_amount_apartment = nights_count * price_per_night_apartment
print(f'Apartment: {total_amount_apartment:.2f} lv.')
print(f'Studio: {total_amount_studio:.2f} lv.')
