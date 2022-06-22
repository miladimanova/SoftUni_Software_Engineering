length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage_taken_by_else = float(input())

aquarium_size_cm = length_cm * width_cm * height_cm
aquarium_size_liters = aquarium_size_cm / 1000

water_to_be_filled_in_litres = aquarium_size_liters - aquarium_size_liters * percentage_taken_by_else / 100

print(water_to_be_filled_in_litres)