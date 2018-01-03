# You can use lru cache (least resource usage) class from functools
# refer the youtube link for the same: https://youtu.be/Qk0zUZW-U_M?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-
febonacci_cache = {}

def febonacci(n):
    if (type(n) != int):
        raise TypeError("n must be a positive integer")
    if ( n < 1):
        raise ValueError("n must be a positive number and greater than zero")
    if n in febonacci_cache:
        return febonacci_cache[n]

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value =  febonacci(n-1) + febonacci(n-2)

    # cache the value into febonacci_cache and then return it
        febonacci_cache[n] = value
        return febonacci_cache[n]

# for n in range ( 1, 1001):
   # print(n, " : " , febonacci(n))

print(febonacci(9))