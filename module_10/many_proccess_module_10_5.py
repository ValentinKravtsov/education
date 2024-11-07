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
    process1 = multiprocessing.Process(target=read_info, args=(filenames[0], ))
    process2 = multiprocessing.Process(target=read_info, args=(filenames[1], ))
    process3 = multiprocessing.Process(target=read_info, args=(filenames[2], ))
    process4 = multiprocessing.Process(target=read_info, args=(filenames[3], ))
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    time_end = time.time()
    print('Многопроцессорный:', time_end - time_start)
