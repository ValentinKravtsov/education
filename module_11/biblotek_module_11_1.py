import requests
import matplotlib.pyplot as plt
import numpy as np

req = requests.get('https://mail.ru/')
print(req.url)
print(req.cookies)
print(req.history)

np_1 = np.array([254, 6767, 36546, 33, 78, 313, 357, 676, 9987, 999])
np_2 = np.array([1, 676, 693, 13])

print(f'Отсортированный массив: {np.sort(np_1)}')
print(f'Объединённый массив: {np.concatenate((np_1, np_2))}')
print(f'Максимальное значение 1 массива: {np_1.max()}, минимальное значение 1 массива: {np_1.min()}')
print(f'Максимальное значение 2 массива: {np_2.max()}, минимальное значение 2 массива: {np_2.min()}')


x = [20, 17, 40, 66, 46]
y = [33, 2, 40, 44, 89]
plt.plot(x, y, label='Line', linestyle='--', color='red')
# plt.show()

plt.scatter(x, y, color='green')
# plt.show()

plt.bar(x, y, color='black')
plt.show()
