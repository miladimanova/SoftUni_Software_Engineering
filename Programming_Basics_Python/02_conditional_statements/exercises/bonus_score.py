number = int(input())
bonus = 0


if number <= 100:
    bonus += 5

elif 100 < number <= 1000:
    bonus += number * (20 / 100)

else:
    bonus += number * (10 / 100)

if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2

total_amount = bonus + number

print(bonus)
print(total_amount)
