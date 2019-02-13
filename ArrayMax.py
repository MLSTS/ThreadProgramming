#!/usr/bin/python
import multiprocessing
import random

NUM_THREADS = 4

def run(id, data, maxValue):
    chunkSize = int (len(data) / NUM_THREADS)
    start = chunkSize * id
    end = chunkSize * (id + 1)
    
    maxValue[id] = max(data[start:end])

if __name__ == '__main__':
    data = multiprocessing.Array('i', 1000) # i = integer, d = double
    maxValue = multiprocessing.Array('i', 4)

    for i in range(len(data)):
        data[i] = random.randint(0,1000000)

    procs = []
    for i in range(NUM_THREADS):
        p = multiprocessing.Process( target=run, args=(i, data, maxValue))
        procs.append(p)
        p.start()

    for i in range(NUM_THREADS):
        procs[i].join()

    print(data[:])
    print("--------------------------------------------------")
    print("Maximum value in each threads: ")
    print(maxValue[:])
    print("Global maximum value: %d" % (max(maxValue)))