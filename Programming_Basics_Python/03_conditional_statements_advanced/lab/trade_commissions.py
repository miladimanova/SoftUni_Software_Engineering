city = input()
s = float(input())
commission = 0

if city != 'Sofia' and city != 'Varna' and city != 'Plovdiv':
    print('error')
elif s < 0:
    print('error')
elif city == 'Sofia':
    if 0 <= s <= 500:
        commission = 0.05
    elif 500 < s <= 1000:
        commission = 0.07
    elif 1000 < s <= 10000:
        commission = 0.08
    elif s > 10000:
        commission = 0.12
    com = s * commission
    print(f'{com:2.2f}')
elif city == 'Varna':
    if 0 <= s <= 500:
        commission = 0.045
    elif 500 < s <= 1000:
        commission = 0.075
    elif 1000 < s <= 10000:
        commission = 0.10
    elif s > 10000:
        commission = 0.13
    com = s * commission
    print(f'{com:2.2f}')
elif city == 'Plovdiv':
    if 0 <= s <= 500:
        commission = 0.055
    elif 500 < s <= 1000:
        commission = 0.08
    elif 1000 < s <= 10000:
        commission = 0.12
    elif s > 10000:
        commission = 0.145
    com = s * commission
    print(f'{com:2.2f}')
