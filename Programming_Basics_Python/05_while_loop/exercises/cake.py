width_cake = int(input())
length_cake = int(input())
count_of_cake_pieces = width_cake * length_cake

while True:
    taken_pieces_of_cake = input()

    if taken_pieces_of_cake == 'STOP':
        print(f'{count_of_cake_pieces} pieces are left.')
        break

    count_of_cake_pieces -= int(taken_pieces_of_cake)

    if count_of_cake_pieces <= 0:
        print(f'No more cake left! You need {abs(count_of_cake_pieces)} pieces more.')
        break
