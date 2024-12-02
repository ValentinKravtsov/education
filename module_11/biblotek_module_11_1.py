import requests
import matplotlib.pyplot as plt
import numpy as np

req = requests.get('https://mail.ru/')
print(req.url)  #вывод url-адреса запроса
print(req.cookies)  # вывод coockie, установленные сервером
print(req.history)  # содержит объекты редиректа (перевод на другую страницу)

np_1 = np.array([254, 6767, 36546, 33, 78, 313, 357, 676, 9987, 999])
np_2 = np.array([1, 676, 693, 13])

print(f'Отсортированный массив: {np.sort(np_1)}')  # сортирует массив от меньшего значения к большему
print(f'Объединённый массив: {np.concatenate((np_1, np_2))}')  # объединяет один массив с другим (добавляет его в конец)
# метод max выводит максимальное значение в массиве,
# метод min выводит минимальное значение в массиве
print(f'Максимальное значение 1 массива: {np_1.max()}, минимальное значение 1 массива: {np_1.min()}')
print(f'Максимальное значение 2 массива: {np_2.max()}, минимальное значение 2 массива: {np_2.min()}')


x = [20, 17, 40, 66, 46]
y = [33, 2, 40, 44, 89]

# делает линейный график
# x, y - первый аргумент ось x, второй - ось y (кол-во значений в списках должно быть одинаковым)
# label - название "легенды" для данного графика
# linestyle - стиль линейного графика, как будет отображена линия
# color - цвет линии
plt.plot(x, y, label='Line', linestyle='dotted', color='red')

# делает точки на графике
# x, y - первый аргумент ось x, второй - ось y (кол-во значений в списках должно быть одинаковым)
# label - название "легенды" для данного графика
# color - цвет точек
plt.scatter(x, y, label='Point', color='green')

# делает столбчатую диаграмму на графике
# x, y - первый аргумент ось x, второй - высота столбца по оси y (кол-во значений в списках должно быть одинаковым)
# label - название "легенды" для данного графика
# color - цвет столбцов
plt.bar(x, y, label='Tower', color='black')

plt.legend()  # выводит легенду на экран
plt.show()  # выводит график на экран (требует установки дополнительного модуля PyQt5)