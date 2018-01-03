import random

for n in range(10):
    print((random.random()*4)+3)
    print(random.uniform(3,4))
    print(random.normalvariate(4,10))
    print(random.randint(1,6))
#you can also use choice function to make a random choice from list of element
# random() and uniform() functions are both uniform distributions
# random function is basis for many other functions in random
