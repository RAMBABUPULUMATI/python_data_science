import multiprocessing
import time

def __sum__(num):
    sum = 0
    for i in range(num):
        sum += i*i
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p = multiprocessing.Pool(processes=4)
    result = p.map(__sum__,range(10000))
    p.close()
    p.join()

    print('pool time is :' ,time.time() - t1)

    t2 = time.time()
    result = []
    for i in range(1000):
        result.append(__sum__(i))

    print('serial time is :', time.time() - t2)
