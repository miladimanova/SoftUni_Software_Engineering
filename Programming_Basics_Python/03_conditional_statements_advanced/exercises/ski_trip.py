days_of_stay = int(input())
type_of_room = input()
rating = input()
costs = 0
number_of_nights = days_of_stay - 1

if type_of_room == 'room for one person':
    costs = 18 * number_of_nights
elif type_of_room == 'apartment':
    if days_of_stay < 10:
        costs = (number_of_nights * 25) - (number_of_nights * 25 * 0.30)
    elif 10 <= days_of_stay <= 15:
        costs = (number_of_nights * 25) - (number_of_nights * 25 * 0.35)
    elif days_of_stay > 15:
        costs = (number_of_nights * 25) - (number_of_nights * 25 * 0.50)
elif type_of_room == 'president apartment':
    if days_of_stay < 10:
        costs = (number_of_nights * 35) - (number_of_nights * 35 * 0.10)
    elif 10 >= days_of_stay <= 15:
        costs = (number_of_nights * 35) - (number_of_nights * 35 * 0.15)
    elif days_of_stay > 15:
        costs = (number_of_nights * 35) - (number_of_nights * 35 * 0.20)
if rating == 'positive':
    costs += costs * 0.25
elif rating == 'negative':
    costs -= costs * 0.10
print(f'{costs:.2f}')



