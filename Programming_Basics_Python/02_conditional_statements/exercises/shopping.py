budget = float(input())
n_cards_count = int(input())
m_processor_count = int(input())
p_ram_count = int(input())

price_n = 250
price_m = 0.35 * (price_n * n_cards_count)
price_p = 0.10 * (price_n * n_cards_count)

total_amount = n_cards_count * price_n + m_processor_count * price_m + p_ram_count * price_p

if n_cards_count > m_processor_count:
     total_amount = total_amount - (total_amount * 0.15)

difference = abs(budget - total_amount)

if total_amount <= budget:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')

