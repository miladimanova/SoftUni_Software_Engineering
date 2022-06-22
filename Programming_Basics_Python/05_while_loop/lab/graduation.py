name_student = input()
year = 1
sum = 0
average_grade = 0
bad_grade_counter = 0

while year <= 12:
    if bad_grade_counter > 1:
        break
    grade = float(input())
    if grade < 4:
        bad_grade_counter += 1
        continue
    sum += grade
    year += 1

if bad_grade_counter > 1:
    print(f'{name_student} has been excluded at {year} grade')
else:
    average_grade = sum / 12
    print(f'{name_student} graduated. Average grade: {average_grade:.2f}')