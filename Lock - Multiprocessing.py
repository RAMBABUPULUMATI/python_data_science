import time
import multiprocessing

def bank_deposite(balance,lock):
    for i in range(100):
        time.sleep(0.02)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def bank_withdrawal(balance,lock):
    for i in range(100):
        time.sleep(0.02)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == "__main__":
    balance =multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=bank_deposite,args=(balance,lock))
    p2 = multiprocessing.Process(target=bank_withdrawal,args=(balance,lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Value of balance available in account is ",balance.value)