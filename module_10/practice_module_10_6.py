import multiprocessing as mp
from asyncio import timeout
import time

from PIL import Image
from queue import Empty

def resize_image(image_paths, queue):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((400, 600))
        queue.put((image_path, image))

def change_color(queue):
    while True:
        try:
            image_path, image = queue.get(timeout=1)
        except Empty:
            break
        image = image.convert('L')
        image.save(image_path)


if __name__ == '__main__':
    data = []
    queue = mp.Queue()

    for image in range(1, 15):
        data.append(f'./images/{image}.jpg')

    resize_process = mp.Process(target=resize_image, args=(data, queue, ))
    change_process = mp.Process(target=change_color, args=(queue, ))

    start = time.time()

    resize_process.start()
    change_process.start()

    resize_process.join()
    change_process.join()

    finish = time.time()

    print(f'Время: {finish - start}')
