input_amount = input()
balance = 0

while input_amount != 'NoMoreMoney':
    amount = float(input_amount)
    if amount < 0:
        print(f'Invalid operation!')
        break
    balance += amount
    print(f'Increase: {amount:.2f}')

    input_amount = input()

print(f'Total: {balance:.2f}')

