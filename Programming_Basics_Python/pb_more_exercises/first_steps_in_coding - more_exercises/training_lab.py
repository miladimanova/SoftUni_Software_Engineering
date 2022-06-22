w_length_meters = float(input())
h_width_meters = float(input())
hallway_cm = 100
door_cm = 1
stage = 2
w_working_space = 120
h_working_space = 70
w_length_cm = w_length_meters * 100
h_width_cm = h_width_meters * 100

current_width = h_width_cm - hallway_cm
h_working_stations = current_width // h_working_space

w_working_stations = w_length_cm // w_working_space

total_working_stations = h_working_stations * w_working_stations - door_cm - stage
print(f'{total_working_stations:.0f}')


