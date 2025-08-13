import time
import random
import math


def c_to_f(c):	# convert Centigrade to Farenheit
    return c*9.0/5 + 32

def mysum(x):	# 
    total = 0
    for i in range (x+1):
        total += i
    return total

def square(n):	# square a number 'slowly'
    sqsum = 0
    for i in range (n):
        for j in range (n):
            sqsum += 1
    return sqsum
    
def time_wrapper(f, L):
    print('Timing', f.__name__)
    for i in L:
        t = time.time()
        f(i)
        dt = time.time()-t
        print (f"{f.__name__}({i}) took {dt} sec")
        
# create an array (L_N) 8 elements each one 10 time bigger
L_N = [1]
for i in range(8):
    L_N.append(L_N[-1]*10)
    
time_wrapper(c_to_f, L_N)	# convert c to f using the array
time_wrapper(mysum, L_N)
time_wrapper(square, L_N)	# Tis takes a looong time on a slow Pi!
