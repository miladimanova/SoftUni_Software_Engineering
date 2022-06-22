degrees = float(input())

status = str

if 26 <= degrees <= 35:
    status = 'Hot'
elif 20.1 <= degrees <= 25.9:
    status = 'Warm'
elif 15 <= degrees <= 20:
    status = 'Mild'
elif 12 <= degrees <= 14.9:
    status = 'Cool'
elif 5 <= degrees <= 11.9:
    status = 'Cold'
else:
    status = 'unknown'

print(status)