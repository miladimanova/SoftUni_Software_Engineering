start_interval = int(input())
final_interval = int(input())
magic_number = int(input())
combination_count = 0
condition = False

for number1 in range(start_interval, final_interval + 1):
    for number2 in range(start_interval, final_interval + 1):
        result = number1 + number2
        combination_count += 1
        if result == magic_number:
            condition = True
            break
    if condition:
        print(f'Combination N:{combination_count} ({number1} + {number2} = {magic_number})')
        break

if not condition:
    print(f'{combination_count} combinations - neither equals {magic_number}')