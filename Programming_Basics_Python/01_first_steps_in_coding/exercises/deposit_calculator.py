deposited_amount = float(input())
deposit_period_months = int(input())
annual_interest_rate = float(input())

annual_interest = deposited_amount * (annual_interest_rate / 100)
interest_per_month = annual_interest / 12

amount_at_the_end_of_the_deposit_period = deposited_amount + deposit_period_months * interest_per_month
print(amount_at_the_end_of_the_deposit_period)