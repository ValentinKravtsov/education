number_1 = input('Введите 1 число: ')
number_2 = input('Введите 2 число: ')
number_3 = input('Введите 3 число: ')

if number_1 == number_2 and number_1 == number_3:
    print('Все 3 числа равны.')
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print('2 числа равны')
else:
    print('Числа не равны')
