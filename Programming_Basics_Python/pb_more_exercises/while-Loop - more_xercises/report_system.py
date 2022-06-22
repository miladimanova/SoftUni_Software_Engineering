expected_savings = float(input())
payments_counter = 0
cs_transactions_counter = 0
cc_transactions_counter = 0
cs_payment = 0
cc_payment = 0
total_amount = 0
amount_not_collected = True
while expected_savings > total_amount:
    price_per_item = input()
    if price_per_item == 'End':
        print('Failed to collect required money for charity.')
        break
    payments_counter += 1
    if payments_counter % 2 == 0:
        if int(price_per_item) < 10:
            print('Error in transaction!')
        else:
            cc_transactions_counter += 1
            cc_payment += int(price_per_item)
            total_amount += int(price_per_item)
            print('Product sold!')
    elif payments_counter % 2 != 0:
        if int(price_per_item) > 100:
            print('Error in transaction!')
        else:
            cs_transactions_counter += 1
            cs_payment += int(price_per_item)
            total_amount += int(price_per_item)
            print('Product sold!')
    if expected_savings <= total_amount:
        amount_not_collected = False
        average_cs = cs_payment / cs_transactions_counter
        average_cc = cc_payment / cc_transactions_counter
        break
if not amount_not_collected:
    print(f'Average CS: {average_cs:.2f}')
    print(f'Average CC: {average_cc:.2f}')

