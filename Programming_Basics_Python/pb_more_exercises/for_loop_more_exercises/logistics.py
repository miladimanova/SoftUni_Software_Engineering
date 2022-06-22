load_count = int(input())
counter_van = 0
counter_truck = 0
counter_train = 0
total_price_van = 0
total_price_truck = 0
total_price_train = 0

for transport_type in range(load_count):
    weight_tons = float(input())
    if weight_tons <= 3:
        transport_type = 'van'
        price_per_ton = 200
        counter_van += weight_tons
        total_price_van = counter_van * price_per_ton
    elif 4 <= weight_tons <= 11:
        transport_type = 'truck'
        price_per_ton = 175
        counter_truck += weight_tons
        total_price_truck = counter_truck * price_per_ton
    elif weight_tons >= 12:
        transport_type = 'train'
        price_per_ton = 120
        counter_train += weight_tons
        total_price_train = counter_train * price_per_ton
all_loads = counter_van + counter_truck + counter_train
average_price_per_ton = (total_price_van + total_price_truck + total_price_train) / all_loads
print(f'{average_price_per_ton:.2f}')
print(f'{(counter_van / all_loads * 100):.2f}%')
print(f'{(counter_truck / all_loads * 100):.2f}%')
print(f'{(counter_train / all_loads * 100):.2f}%')