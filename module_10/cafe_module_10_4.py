from queue import Queue
from threading import Thread
from time import sleep
from random import randint

class Table:
    guest = None

    def __init__(self, number):
        self.number = number

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.q = Queue()

    def guest_arrival(self, *guests):
        for i in range(len(guests)):
            try:
                self.tables[i].guest = guests[i]
                print(f'{guests[i].name} сел(-а) за стол номер {tables[i].number}')
            except:
                self.q.put(guests[i])
                print(f'{guests[i].name} в очереди')


    def discuss_guests(self):
        for table in self.tables:
            table.guest.start()

        key = True
        while key:
            table_free = 0
            for table in self.tables:
                if table.guest.is_alive():
                    continue
                elif not self.q.empty():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    table.guest = self.q.get()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    table.guest.start()
                table_free += 1
            if table_free == len(self.tables):
                print('Гостей в очереди нет, столы свободны')
                key = False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

