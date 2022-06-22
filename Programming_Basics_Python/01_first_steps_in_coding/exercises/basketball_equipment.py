basketball_training_yearly_fee = int(input())

basketball_sneakers_price = basketball_training_yearly_fee - (40 / 100) * basketball_training_yearly_fee
basketball_dressing_price = basketball_sneakers_price - (20 / 100) * basketball_sneakers_price
ball_for_basketball = (1 / 4) * basketball_dressing_price
basketball_accessories_price = (1 / 5) * ball_for_basketball

total_expense = basketball_training_yearly_fee + basketball_sneakers_price + basketball_dressing_price + \
                ball_for_basketball + basketball_accessories_price

print(total_expense)

