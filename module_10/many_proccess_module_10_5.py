import time, multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            all_data.append(line)



filenames = [f'./files/file {number}.txt' for number in range(1, 5)]
time_start = time.time()
for i in filenames:
    read_info(i)
time_end = time.time()
print('Линейный:', time_end - time_start)


if __name__ == '__main__':
    time_start = time.time()
    proccess1 = multiprocessing.Process(target=read_info, args=(filenames[0], ))
    proccess2 = multiprocessing.Process(target=read_info, args=(filenames[1], ))
    proccess3 = multiprocessing.Process(target=read_info, args=(filenames[2], ))
    proccess1.start()
    proccess2.start()
    proccess3.start()
    proccess1.join()
    proccess2.join()
    proccess3.join()
    time_end = time.time()
    print('Многопроцессорный:', time_end - time_start)
