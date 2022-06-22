fuel_type = input()
liters_in_tank = int(input())

if fuel_type == 'Diesel':
    if liters_in_tank >= 25:
        print(f'You have enough diesel.')
    elif liters_in_tank < 25:
        print(f'Fill your tank with diesel!')
elif fuel_type == 'Gasoline':
    if liters_in_tank >= 25:
        print(f'You have enough gasoline.')
    elif liters_in_tank < 25:
        print(f'Fill your tank with gasoline!')
elif fuel_type == 'Gas':
    if liters_in_tank >= 25:
        print(f'You have enough gas.')
    elif liters_in_tank < 25:
        print(f'Fill your tank with gas!')
else:
    print('Invalid fuel!')