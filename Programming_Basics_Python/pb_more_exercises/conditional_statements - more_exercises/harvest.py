import math

x_sq_m_vineyard = int(input())
y_grapes_per_sq_m = float(input())
z_needed_liters_wine = int(input())
workers_count = int(input())
grape_kg_for_1_liter = 2.5

grape_production = x_sq_m_vineyard * y_grapes_per_sq_m
wine_production = grape_production * 0.40 / grape_kg_for_1_liter
diff = abs(z_needed_liters_wine - wine_production)
if wine_production < z_needed_liters_wine:
    print(f'It will be a tough winter! More {math.floor(diff)} liters wine needed.')
else:
    wine_per_worker = diff / workers_count
    print(f'Good harvest this year! Total wine: {math.floor(wine_production)} liters.')
    print(f'{math.ceil(diff)} liters left -> {math.ceil(wine_per_worker)} liters per person.')