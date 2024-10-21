from random import choice


# 1
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x[0] == y[0], first, second)))


# 2
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf-8')
        file.writelines(map(lambda x: str(x) + '\n', data_set))
        # result = list(map(lambda x: file.write(str(x) + '\n'), data_set))
        # print(list(result))
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# 3
class MysticBall:
    def __init__(self, *args):
        self.words = list(args)

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
