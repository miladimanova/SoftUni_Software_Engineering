import sys
n = int(input())
max_num = -sys.maxsize
sum_num = 0

for num in range(n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    sum_num += current_num
if max_num == sum_num - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs((sum_num - max_num) - max_num)
    print('No')
    print(f'Diff = {diff}')