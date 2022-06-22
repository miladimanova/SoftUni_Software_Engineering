from math import pi
number_r = float(input())

d = 2 * number_r
calculated_perimeter = pi * d
calculated_area = calculated_perimeter * d / 4

print(f'{calculated_area:.2f}')
print(f'{calculated_perimeter:.2f}')