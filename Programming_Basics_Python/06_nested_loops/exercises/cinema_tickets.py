students_ticket_counter = 0
standard_ticket_counter = 0
kid_ticket_counter = 0
total_ticket_counter = 0
command = input()
while command != 'Finish':
    movie_name = command
    free_sets = int(input())
    sold_tickets = 0
    total_seats = free_sets
    while free_sets > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'standard':
            standard_ticket_counter += 1
        elif ticket_type == 'student':
            students_ticket_counter += 1
        elif ticket_type == 'kid':
            kid_ticket_counter += 1
        free_sets -= 1
        sold_tickets += 1
        total_ticket_counter += 1
    hall_occupancy = sold_tickets / total_seats * 100
    print(f'{movie_name} - {hall_occupancy:.2f}% full.')
    command = input()
students_percent = students_ticket_counter / total_ticket_counter * 100
standard_percent = standard_ticket_counter / total_ticket_counter * 100
kids_percent = kid_ticket_counter / total_ticket_counter * 100
print(f'Total tickets: {total_ticket_counter}')
print(f'{students_percent:.2f}% student tickets.')
print(f'{standard_percent:.2f}% standard tickets.')
print(f'{kids_percent:.2f}% kids tickets.')
