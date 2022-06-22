count_of_chicken_menus = int(input())
count_of_fish_menus = int(input())
count_of_vegetarian_menus = int(input())

total_price_main_course = count_of_chicken_menus * 10.35 + count_of_fish_menus * 12.40 + \
                          count_of_vegetarian_menus * 8.15

dessert_price = (20 / 100) * total_price_main_course

final_order_price = total_price_main_course + dessert_price + 2.50

print(final_order_price)