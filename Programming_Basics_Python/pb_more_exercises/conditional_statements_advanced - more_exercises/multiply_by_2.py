condition = True
while condition:
    number = float(input())
    if number < 0:
        condition = False
        print('Negative number!')
        break
    print(f'Result: {(number * 2) :.2f}')
