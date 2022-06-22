detergent_bottles_count = int(input())
ml_per_bottle = 750
ml_per_plate = 5
ml_per_pot = 15
ml_detergent = detergent_bottles_count * ml_per_bottle
total_used_detergent = 0
plates_counter = 0
pots_counter = 0
dishes_set_counter = 0
dishes = 0
while True:
    dishes = input()
    if dishes == 'End':
        break
    dishes_set_counter += 1
    if dishes_set_counter % 3 == 0:
        pots_counter += int(dishes)
    else:
        plates_counter += int(dishes)
    total_used_detergent = plates_counter * ml_per_plate + pots_counter * ml_per_pot
    diff = abs(total_used_detergent - ml_detergent)
if total_used_detergent <= ml_detergent:
    print('Detergent was enough!')
    print(f'{plates_counter} dishes and {pots_counter} pots were washed.')
    print(f'Leftover detergent {diff} ml.')
else:
    print(f'Not enough detergent, {diff} ml. more necessary!')

