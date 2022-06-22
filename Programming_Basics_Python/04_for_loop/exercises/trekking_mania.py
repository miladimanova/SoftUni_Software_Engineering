groups_of_climbers_count = int(input())
total_count_people = 0
musala_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
for i in range(groups_of_climbers_count):
    number_of_climbers_per_group = int(input())
    total_count_people += number_of_climbers_per_group

    if number_of_climbers_per_group <= 5:
        musala_climbers += number_of_climbers_per_group
    elif 6 <= number_of_climbers_per_group <= 12:
        monblan_climbers += number_of_climbers_per_group
    elif 13 <= number_of_climbers_per_group <= 25:
        kilimandjaro_climbers += number_of_climbers_per_group
    elif 26 <= number_of_climbers_per_group <= 40:
        k2_climbers += number_of_climbers_per_group
    elif number_of_climbers_per_group >= 40:
        everest_climbers += number_of_climbers_per_group

print(f'{musala_climbers / total_count_people * 100:.2f}%')
print(f'{monblan_climbers / total_count_people * 100:.2f}%')
print(f'{kilimandjaro_climbers / total_count_people * 100:.2f}%')
print(f'{k2_climbers / total_count_people * 100:.2f}%')
print(f'{everest_climbers / total_count_people * 100:.2f}%')