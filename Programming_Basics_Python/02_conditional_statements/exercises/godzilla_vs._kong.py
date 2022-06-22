movie_budget = float(input())
statists_count = int(input())
single_cloth_price = float(input())

movie_decor = movie_budget * 0.10
total_cloth_price = single_cloth_price * statists_count

if statists_count > 150:
    total_cloth_price -= total_cloth_price * (10 / 100)

costs = total_cloth_price + movie_decor
remainder = abs(movie_budget - costs)

if costs > movie_budget:
    print('Not enough money!')
    print(f'Wingard needs {remainder:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {remainder:.2f} leva left.')