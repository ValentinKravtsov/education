number_hidden = int(input('Введите число от 3 до 20: '))
list_numbers_answer = []

if 3 <= number_hidden <= 20:
    for i in range(1, number_hidden + 1):
        for j in range(1, number_hidden):
            if i == j:
                continue
            if number_hidden % (i + j) == 0:
                merge_number = [i, j]
                merge_number.sort()

                key = 0
                for k in list_numbers_answer:
                    if merge_number == k:
                        key = 1
                if key != 1:
                    list_numbers_answer.append(merge_number)

else:
    print('Не верное число')

numbers_answer = []
for list_numbers in list_numbers_answer:
    numbers_answer.append(''.join(map(str, list_numbers)))

print(int(''.join(numbers_answer)))
