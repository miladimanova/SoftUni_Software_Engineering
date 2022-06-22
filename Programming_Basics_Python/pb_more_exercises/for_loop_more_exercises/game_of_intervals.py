number_of_game_moves = int(input())
result = 0
number_counter_1 = 0
number_counter_2 = 0
number_counter_3 = 0
number_counter_4 = 0
number_counter_5 = 0
number_counter_6 = 0
for num in range(1, number_of_game_moves + 1):
    number = int(input())
    if 0 <= number <= 9:
        number_counter_1 += 1
        result += number * 0.20
    elif 10 <= number <= 19:
        number_counter_2 += 1
        result += number * 0.30
    elif 20 <= number <= 29:
        number_counter_3 += 1
        result += number * 0.40
    elif 30 <= number <= 39:
        number_counter_4 += 1
        result += 50
    elif 40 <= number <= 50:
        number_counter_5 += 1
        result += 100
    else:
        number_counter_6 += 1
        result /= 2
total_number_counter = number_counter_1 + number_counter_2 + number_counter_3 + number_counter_4 + number_counter_5 + \
                       number_counter_6
print(f"{result:.2f}")
print(f"From 0 to 9: {(number_counter_1 / total_number_counter * 100):.2f}%")
print(f"From 10 to 19: {(number_counter_2 / total_number_counter * 100):.2f}%")
print(f"From 20 to 29: {(number_counter_3 / total_number_counter * 100):.2f}%")
print(f"From 30 to 39: {(number_counter_4 / total_number_counter * 100):.2f}%")
print(f"From 40 to 50: {(number_counter_5 / total_number_counter * 100):.2f}%")
print(f"Invalid numbers: {(number_counter_6 / total_number_counter * 100):.2f}%")
