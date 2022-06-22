amount_back = int(float(input()) * 100)
number_of_coins = 0

while amount_back > 0:
    if amount_back >= 200:
        amount_back -= 200
    elif amount_back >= 100:
        amount_back -= 100
    elif amount_back >= 50:
        amount_back -= 50
    elif amount_back >= 20:
        amount_back -= 20
    elif amount_back >= 10:
        amount_back -= 10
    elif amount_back >= 5:
        amount_back -= 5
    elif amount_back >= 2:
        amount_back -= 2
    elif amount_back >= 1:
        amount_back -= 1

    number_of_coins += 1
print(number_of_coins)
