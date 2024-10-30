import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight(self.name, self.power, self.enemy)

    def fight(self, name, power, enemy):
        days = 0
        while enemy > 0:
            sleep(1)
            enemy -= power
            days += 1
            print(f'{name} сражается {days} день(дня)..., осталось {enemy} воинов')

        print(f'{name} одержал победу спустя {days} дня(дней)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Битвы закончились!')