v_pool_liters = int(input())
p1_debit_1st_pipe_per_hour = int(input())
p2_debit_2nd_pipe_per_hour = int(input())
h_worker_absence_hours = float(input())

p1_liters = p1_debit_1st_pipe_per_hour * h_worker_absence_hours
p2_liters = p2_debit_2nd_pipe_per_hour * h_worker_absence_hours
total_liters_filled = p1_liters + p2_liters

if total_liters_filled <= v_pool_liters:
    percent_pool = total_liters_filled / v_pool_liters * 100
    percent_p1 = p1_liters / total_liters_filled * 100
    percent_p2 = p2_liters / total_liters_filled * 100
    print(f'The pool is {percent_pool:.2f}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.')
elif total_liters_filled > v_pool_liters:
    diff = abs(total_liters_filled - v_pool_liters)
    print(f'For {h_worker_absence_hours} hours the pool overflows with {diff:.2f} liters.')