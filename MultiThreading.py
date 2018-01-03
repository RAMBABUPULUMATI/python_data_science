import time
import threading

def calc_square(number):
    print("calculate square")
    for n in number:
        time.sleep(0.2)
        print('square of ', n ,'is:', n*n)

def calc_cube(number):
    print("calculate cubes")
    for n in number:
        time.sleep(0.2)
        print('cubes of ',n,'is:', n*n*n)

arr = [2,3,4,5,6,7,8,9,10]
t =  time.time()


t1 = threading.Thread(target = calc_square, args=(arr,))
t2 = threading.Thread(target = calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()


print("Total time taken to finish square and cube is:" , time.time() - t )

