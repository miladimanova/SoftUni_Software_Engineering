price_per_page = float(input())
price_per_cover_page = float(input())
percent_print_paper_discount = int(input())
price_design = float(input())
percent_amount_to_pay_be_team = int(input())
pages = 899
covers = 2
total_print_paper = pages * price_per_page + covers * price_per_cover_page
print_discount = total_print_paper * percent_print_paper_discount / 100
total_print_price = total_print_paper - print_discount
total_amount = total_print_price + price_design
amount_by_team = total_amount * percent_amount_to_pay_be_team / 100
money = total_amount - amount_by_team

print(f'Avtonom should pay {money:.2f} BGN.')