allowed_bad_grades_counter = int(input())
bad_grade_counter = 0
total_grade_counter = 0
grade_sum = 0
last_task = str
has_failed = True

while bad_grade_counter < allowed_bad_grades_counter:
    task_name = input()
    if task_name == 'Enough':
        has_failed = False
        break

    grade = float(input())

    if grade <= 4:
        bad_grade_counter += 1

    grade_sum += grade
    total_grade_counter += 1
    last_task = task_name
    average_score = grade_sum / total_grade_counter



if has_failed:
    print(f'You need a break, {bad_grade_counter} poor grades.')


else:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {total_grade_counter}')
    print(f'Last problem: {last_task}')

