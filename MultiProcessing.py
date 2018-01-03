import time
import multiprocessing

sequence_square = []

def calc_square(num):
    global sequence_square
    for n in num:
        print('square of ',n,'is: ',n*n)
        sequence_square.append(n*n)
    print('with in process result set' + str(sequence_square))

def calc_cube(num):
    for n in num:
        print('cubes of ',n,'is: ',n*n*n)

if __name__ == "__main__":
    arr = [2,3,4,5,6,7,8,9]

    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
    print("square are ", sequence_square)
