stadium_capacity = int(input())
total_fens_count = int(input())
a_fens_count = 0
b_fens_count = 0
v_fens_count = 0
g_fens_count = 0
for fens in range(1, total_fens_count + 1):
    sector = input()
    if sector == 'A':
        a_fens_count += 1
    elif sector == 'B':
        b_fens_count += 1
    elif sector == 'V':
        v_fens_count += 1
    elif sector == 'G':
        g_fens_count += 1
print(f'{(a_fens_count / total_fens_count * 100):.2f}%')
print(f'{(b_fens_count / total_fens_count * 100):.2f}%')
print(f'{(v_fens_count / total_fens_count * 100):.2f}%')
print(f'{(g_fens_count / total_fens_count * 100):.2f}%')
print(f'{(total_fens_count / stadium_capacity * 100):.2f}%')