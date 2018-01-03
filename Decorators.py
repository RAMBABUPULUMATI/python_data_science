import time

def time_func(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start)*1000))
        return result
    return wrapper

@time_func
def calc_square(num):
    result= []
    for i in num:
        result.append(i*i)
    return result

@time_func
def calc_cubes(num):
    result = []
    for i in num:
        result.append(i * i * i)
    return result

arr = range(1,10000)

out_square = calc_square(arr)
out_cubes = calc_cubes(arr)