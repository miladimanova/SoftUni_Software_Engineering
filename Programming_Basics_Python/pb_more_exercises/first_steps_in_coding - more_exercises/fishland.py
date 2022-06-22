skumriya_price_per_kilo = float(input())
caca_per_kilo = float(input())
palamud_kilos = float(input())
safrid_kilos = float(input())
midi_kilos = float(input())

price_palamud = mackerel_price_per_kilo * 0.60 + mackerel_price_per_kilo
price_safrid = sprat_price_per_kilo * 0.80 + sprat_price_per_kilo
price_midi = 7.50

total_account = price_bonito * bonito_kilos + price_horse_mackerel * horse_mackerel_kilos + price_mussels * \
                mussels_kilos

print(f'{total_account:.2f}')


