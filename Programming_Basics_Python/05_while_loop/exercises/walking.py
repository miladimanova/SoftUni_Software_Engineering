steps = 0

while steps < 10000:
    current_steps = input()
    if current_steps == 'Going home':
        add_steps = int(input())
        steps += add_steps
        break
    steps += int(current_steps)

diff = int(abs(steps - 10000))

if steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')
