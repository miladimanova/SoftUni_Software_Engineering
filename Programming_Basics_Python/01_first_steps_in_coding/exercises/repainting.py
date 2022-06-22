nylon_quantity_square_meters = int(input())
paint_quantity_litters = int(input())
solvent_quantity = int(input())
workers_working_hours = int(input())

nylon = (nylon_quantity_square_meters + 2) * 1.50
paint = (paint_quantity_litters + (10 / 100) * paint_quantity_litters) * 14.50

total_amount_supplies = nylon + paint + solvent_quantity * 5 + 0.40
workers_payment_per_hour = total_amount_supplies * (30 / 100)
total_amount_expenditure = total_amount_supplies + workers_working_hours * workers_payment_per_hour

print(total_amount_expenditure)
