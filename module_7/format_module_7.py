team1 = 'Мастера кода'
team2 = 'Волшебники данных'

team1_num = 5
team2_num = 6

team1_time = 1552.512
team2_time = 2153.31451

score_1 = 40
score_2 = 42

print("В команде %s участников: %s ! " % (team1, team1_num))
print("Итого сегодня в командах участников: %s и %s ! " % (team1_num, team2_num))

print("Команда {} решила задач: {} !".format(team2, score_2))
print("{} решили задачи за: {} c !".format(team2, team1_time))

print(f"Команды решили {score_1} и {score_2} задач.")
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f"Результат битвы: победа команды {team1}!")
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f"Результат битвы: победа команды {team1}!")
else:
    print('Ничья!')

