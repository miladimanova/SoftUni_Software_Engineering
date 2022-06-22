x_house_height = float(input())
y_length_side_wall = float(input())
h_height_triangle_roof_wall = float(input())

rectangular_door_size = 1.2 * 2
front_wall_size = x_house_height ** 2 - rectangular_door_size
back_wall_size = x_house_height ** 2
square_window = 1.5 ** 2
side_walls = x_house_height * y_length_side_wall * 2 - square_window * 2

total_wall_size = front_wall_size + back_wall_size + side_walls

roof_rectangles = 2 * (x_house_height * y_length_side_wall)
roof_triangles = 2 * (x_house_height * h_height_triangle_roof_wall / 2)

total_roof_size = roof_triangles + roof_rectangles

litres_green_paint = total_wall_size / 3.4
litres_red_paint = total_roof_size / 4.3

print(f'{litres_green_paint:.2f}')
print(f'{litres_red_paint:.2f}')