name_actor = input()
points_academy = float(input())
count_of_jury_members = int(input())

for current_points in range(count_of_jury_members):
    jury_member_name = input()
    jury_rating_points = float(input())
    given_points = len(jury_member_name) * jury_rating_points / 2
    points_academy += given_points
    if points_academy > 1250.5:
        break
if points_academy > 1250.5:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {points_academy:.1f}!')
else:
    diff = 1250.5 - points_academy
    print(f'Sorry, {name_actor} you need {diff:.1f} more!')
