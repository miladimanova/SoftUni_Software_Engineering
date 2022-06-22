period_in_days = int(input())
checked_patients_per_day = 0
not_checked_patients_per_day = 0

for day in range(1, period_in_days + 1):
    number_of_patients = int(input())
    if day >= 3 or day % 5 == 3 and not_checked_patients_per_day > checked_patients_per_day:
        if number_of_patients >= 8:
            checked_patients_per_day += 8
            not_checked_patients_per_day += number_of_patients - 8
        else:
            checked_patients_per_day += number_of_patients
    elif day % 5 != 3 and number_of_patients >= 7:
        checked_patients_per_day += 7
        not_checked_patients_per_day += number_of_patients - 7
    else:
        checked_patients_per_day += number_of_patients


print(f'Treated patients: {checked_patients_per_day}.')
print(f'Untreated patients: {not_checked_patients_per_day}.')


