import multiprocessing

def calc_square(num,q):
    for n in num:
        q.put(n*n)

def calc_cube(num,q):
    for n in num:
        q.put(n*n*n)

if __name__ == "__main__":
    arr = [2,3,4,5,6,7,8,9]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square,args=(arr,q))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,q))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    while q.empty() is False:
        print(q.get())
