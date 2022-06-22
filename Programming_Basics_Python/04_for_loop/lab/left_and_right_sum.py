n = int(input())

right_sum = 0
left_sum = 0

for i in range(n):
    current_num = int(input())
    left_sum += current_num

for i in range(n):
    current_num = int(input())
    right_sum += current_num

if left_sum == right_sum:
    sum = (left_sum + right_sum) / 2
    print(f'Yes, sum = {sum:.0f}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')


