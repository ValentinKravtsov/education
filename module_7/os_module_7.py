import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    print(root)
    print(dirs)
    print(files)
    for file in files:
        filepath = os.path.join(os.getcwd(), file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file)))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
