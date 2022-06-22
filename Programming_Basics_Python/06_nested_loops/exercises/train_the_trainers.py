jury_count = int(input())
command_is_not_finish = True
presentations_count = 0
average_grade_student = 0
all_points = 0

while command_is_not_finish:
    presentation_name = input()
    if presentation_name == 'Finish':
        command_is_not_finish = False
        print(f"Student's final assessment is {average_grade_student:.2f}.")
        break
    total_grades_per_presentation = 0
    presentations_count += 1
    for grades in range(1, jury_count + 1):
        given_points = float(input())
        total_grades_per_presentation += given_points
    average_grade_presentation = total_grades_per_presentation / jury_count
    print(f'{presentation_name} - {average_grade_presentation:.2f}.')
    all_points += total_grades_per_presentation
    average_grade_student = all_points / (presentations_count * jury_count)