    number_of_pen_packages = int(input())
    number_of_marker_packages = int(input())
    whiteboard_cleanser_litters = int(input())
    discount_percentage = int(input())

    total_amount_supplies = number_of_pen_packages * 5.8 + number_of_marker_packages * 7.2 + \
                            whiteboard_cleanser_litters * 1.20
    amount_to_pay = total_amount_supplies - (total_amount_supplies * (discount_percentage / 100))
    print(amount_to_pay)
