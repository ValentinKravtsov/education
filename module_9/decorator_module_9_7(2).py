import time
import sys


def func_get_dec(precision):
    print('получили точность, с которой надо выводить результат')
    print('начинаем создавать декоратор')
    def dec(func):
        print(f'декоратор принял на вход функцию, которую надо отдекорировать - {func}')
        print('начинает создавать функцию обёртку')
        def wrapper(*args, **kwargs):
            print('мы в функции-обёртке, которая заместит реальную функцию func')
            print('засекаем время')
            started_at = time.time()
            print('запускаем реальную функцию с переданными в функцию-обёртку параметрами и запоминаем результат')
            result_func = func(*args, **kwargs)
            print('определяем затраченное время и выводим его')
            ended_ed = time.time()
            print(f'вот тут-то и пригодился precision (== {precision}) - он запомнился в замыкании surrogate')
            elapsed = round(ended_ed - started_at, precision)
            print(f'функция работала {elapsed} секунд(ы)')
            print('возвращаем результат, который вернула реальная функция')
            return result_func
        print('декоратор создал функцию-обёртку и возвращает её')
        return wrapper
    print('декоратор создан и пора его вернуть')
    return dec

@func_get_dec(precision=6)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))



sys.set_int_max_str_digits(10**5)

result = digits(3141, 5926, 2718, 2818)
print(result)