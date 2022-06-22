juniors_count = int(input())
seniors_count = int(input())
road_type = input()
total_racers_count = juniors_count + seniors_count
if road_type == 'trail':
    ticket_price_junior = 5.50
    ticket_price_senior = 7
elif road_type == 'cross-country':
    ticket_price_junior = 8
    ticket_price_senior = 9.50
    if total_racers_count >= 50:
        ticket_price_junior -= 8 * 0.25
        ticket_price_senior -= 9.50 * 0.25
elif road_type == 'downhill':
    ticket_price_junior = 12.25
    ticket_price_senior = 13.75
elif road_type == 'road':
    ticket_price_junior = 20
    ticket_price_senior = 21.50
total_amount = ticket_price_junior * juniors_count + ticket_price_senior * seniors_count
expense = total_amount * 0.05
amount_for_charity = total_amount - expense
print(f'{amount_for_charity:.2f}')
