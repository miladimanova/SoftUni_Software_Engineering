students_count = int(input())
students_counter_2s = 0
students_counter_3s = 0
students_counter_4s = 0
students_counter_5s = 0
grade_counter_2s = 0
grade_counter_3s = 0
grade_counter_4s = 0
grade_counter_5s = 0

for student in range(1, students_count + 1):
    student_grade = float(input())
    if 2 <= student_grade <= 2.99:
        students_counter_2s += 1
        grade_counter_2s += student_grade
    elif 3 <= student_grade <= 3.99:
        students_counter_3s += 1
        grade_counter_3s += student_grade
    elif 4 <= student_grade <= 4.99:
        students_counter_4s += 1
        grade_counter_4s += student_grade
    elif student_grade >= 5:
        students_counter_5s += 1
        grade_counter_5s += student_grade
average_result = (grade_counter_5s + grade_counter_4s + grade_counter_3s + grade_counter_2s) / students_count
print(f'Top students: {(students_counter_5s / students_count * 100):.2f}%')
print(f'Between 4.00 and 4.99: {(students_counter_4s / students_count * 100):.2f}%')
print(f'Between 3.00 and 3.99: {(students_counter_3s / students_count * 100):.2f}%')
print(f'Fail: {(students_counter_2s / students_count * 100):.2f}%')
print(f'Average: {average_result:.2f}')