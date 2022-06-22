import math

processors_count_to_produce = int(input())
employees_cont = int(input())
working_days = int(input())
processor_price = 110.1
working_hours = 8
total_working_hours = employees_cont * working_hours * working_days
produced_processors = math.floor(total_working_hours / 3)
diff = abs(processors_count_to_produce - produced_processors)
profit_loss = diff * processor_price
if processors_count_to_produce <= produced_processors:
    print(f'Profit: -> {profit_loss:.2f} BGN')
else:
    print(f'Losses: -> {profit_loss:.2f} BGN')
