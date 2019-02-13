#!/usr/bin/python
import multiprocessing
import random

NUM_THREADS = 4

def run(id, dataA, dataB, dataC, maxValue):
    chunkSize = int (len(dataC) / NUM_THREADS)
    start = chunkSize * id
    end = chunkSize * (id + 1)
    
    for i in range(start,end):
        dataC[i] = dataA[i] + dataB[i]
    maxValue[id] = max(dataC[start:end])

if __name__ == '__main__':
    dataA = multiprocessing.Array('i', 1000) # i = integer, d = double
    dataB = multiprocessing.Array('i', 1000) # i = integer, d = double
    dataC = multiprocessing.Array('i', 1000) # i = integer, d = double
    maxValue = multiprocessing.Array('i', 4)

    for i in range(len(dataA)):
        dataA[i] = i

    for i in range(len(dataB)):
        dataB[i] = i

    procs = []
    for i in range(NUM_THREADS):
        p = multiprocessing.Process( target=run, args=(i, dataA, dataB, dataC, maxValue))
        procs.append(p)
        p.start()

    for i in range(NUM_THREADS):
        procs[i].join()

    print(dataA[:])
    print(dataB[:])
    print(dataC[:])
    print("--------------------------------------------------")
    print("Maximum value in each threads: ")
    print(maxValue[:])
    print("Global maximum value: %d" % (max(maxValue)))