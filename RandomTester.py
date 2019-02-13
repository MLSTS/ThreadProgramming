#!/usr/bin/python
import multiprocessing
import random
import time

NUM_THREADS = 4
NUM_RANDOMS = 100000000
NUM_RANDOMS_PT = int (NUM_RANDOMS / NUM_THREADS)
RESULTS = multiprocessing.Array('i', NUM_THREADS)
THREADS = []

def calculate(id, NUM_RANDOMS_PT, RESULTS):
    count = 0
    for x in range(NUM_RANDOMS_PT):
        rnd = random.random()
        if rnd < 0.5:
            count = count + 1
    RESULTS[id] = count

if __name__ == '__main__':
    st = time.time()

    for i in range(NUM_THREADS):
        p = multiprocessing.Process(target=calculate, args=(i, NUM_RANDOMS_PT, RESULTS))
        THREADS.append(p)
        p.start()
    
    for i in range(NUM_THREADS):
            THREADS[i].join()
    
    et = time.time()
    print("%f %%" % (float(sum(RESULTS))/NUM_RANDOMS))
    print("Number of threads: %d threads." % (NUM_THREADS))
    print("Execution time: %f ms." % ((et-st)*1000))