#!/usr/bin/python
import multiprocessing

NUM_THREADS = 4

def run(id, dataA, dataB, dataC):
    chunkSize = int (len(dataC) / NUM_THREADS)
    start = chunkSize * id
    end = chunkSize * (id + 1)
    
    for i in range(start,end):
        dataC[i] = dataA[i] + dataB[i]

if __name__ == '__main__':
    dataA = multiprocessing.Array('i', 1000) # i = integer, d = double
    dataB = multiprocessing.Array('i', 1000) # i = integer, d = double
    dataC = multiprocessing.Array('i', 1000) # i = integer, d = double

    for i in range(len(dataA)):
        dataA[i] = i

    for i in range(len(dataB)):
        dataB[i] = i

    procs = []
    for i in range(NUM_THREADS):
        p = multiprocessing.Process( target=run, args=(i, dataA, dataB, dataC))
        procs.append(p)
        p.start()

    for i in range(NUM_THREADS):
        procs[i].join()

    print(dataA[:])
    print(dataB[:])
    print(dataC[:])