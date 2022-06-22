import math

magnolias_count = int(input())
zyumbyuls_count = int(input())
roses_count = int(input())
kaktus_count = int(input())
present_price = float(input())

total_income = magnolias_count * 3.25 + zyumbyuls_count * 4 + roses_count * 3.50 + kaktus_count * 8
taxes = total_income * 0.05
profit = total_income - taxes
diff = abs(present_price - profit)

if present_price <= profit:
    print(f'She is left with {math.floor(diff)} leva.')
else:
    print(f'She will have to borrow {math.ceil(diff)} leva.')