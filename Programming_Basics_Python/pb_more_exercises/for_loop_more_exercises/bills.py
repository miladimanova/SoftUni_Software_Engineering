months = int(input())
total_electricity = 0
for expenses in range(1, months + 1):
    electricity_bill = float(input())
    water_bill = 20
    internet_bill = 15
    total_electricity += electricity_bill
total_water = months * water_bill
total_internet = months * internet_bill
total_others = (total_water + total_internet + total_electricity) + 0.20 * (total_water + total_internet + total_electricity)
average = (total_others + total_water + total_internet + total_electricity) / months
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average:.2f} lv")
