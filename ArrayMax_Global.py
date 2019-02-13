#!/usr/bin/python
import multiprocessing
import random
import time

NUM_THREADS = 4

def run(id, data, maxValue, lock):
    chunkSize = int (len(data) / NUM_THREADS)
    start = chunkSize * id
    end = chunkSize * (id + 1)
    
    with lock:
        temp = max(data[start:end])
        if temp > maxValue.value:
            maxValue.value = temp

if __name__ == '__main__':
    st = time.time()
    data = multiprocessing.Array('i', 1000) # i = integer, d = double
    maxValue = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    for i in range(len(data)):
        data[i] = random.randint(0,1000000)

    procs = []
    for i in range(NUM_THREADS):
        p = multiprocessing.Process( target=run, args=(i, data, maxValue, lock))
        procs.append(p)
        p.start()

    for i in range(NUM_THREADS):
        procs[i].join()

    et = time.time()
    print(data[:])
    print("--------------------------------------------------")
    print("Global maximum value: %d" % (maxValue.value))
    print("Execution time: %f ms." % ((et-st)*1000))