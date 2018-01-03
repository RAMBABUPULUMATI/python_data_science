import time
import multiprocessing

def calc_square(num,result):
    for idx, n in enumerate(num):
        result[idx] = n*n

def calc_cube(num):
    for idx, n in enumerate(num):
        print('cubes are :', n*n*n)

if __name__ == "__main__":
    arr = [2,3,4,5,6,7,8,9]
    result = multiprocessing.Array('i',8)
    p1 = multiprocessing.Process(target=calc_square,args=(arr,result))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('squares are :',result[:7])
    print("Done")
