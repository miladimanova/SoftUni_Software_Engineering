price_per_kg_vegetables = float(input())
price_per_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

total_income = price_per_kg_vegetables * total_kg_vegetables / 1.94 + total_kg_fruits * price_per_kg_fruits / 1.94
print(f'{total_income:.2f}')