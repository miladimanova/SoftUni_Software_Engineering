movie = input()
r_count = int(input())
c_count = int(input())
seats = r_count * c_count
price = 0
if movie == 'Premiere':
    price = 12
elif movie == 'Normal':
    price = 7.50
elif movie == 'Discount':
    price = 5
income = seats * price
print(f'{income:.2f} leva')