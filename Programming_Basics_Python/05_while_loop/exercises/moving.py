apartment_length = int(input())
apartment_width = int(input())
apartment_height = int(input())
apartment_size = apartment_height * apartment_length * apartment_width
while True:
    count_of_packages = input()

    if count_of_packages == 'Done':
        print(f'{apartment_size} Cubic meters left.')
        break
    apartment_size -= int(count_of_packages)

    if apartment_size <= 0:
        print(f'No more free space! You need {abs(apartment_size)} Cubic meters more.')
        break
