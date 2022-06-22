n = int(input())
sum_even = 0
sum_odd = 0

for i in range(1, n + 1):
    current_number = int(input())
    if i % 2 == 0:
        sum_even += current_number
    if i % 2 != 0:
        sum_odd += current_number
if sum_odd == sum_even:
    sum = (sum_odd + sum_even) / 2
    print('Yes')
    print(f'Sum = {sum:.0f}')
else:
    diff = abs(sum_even - sum_odd)
    print('No')
    print(f'Diff = {diff}')