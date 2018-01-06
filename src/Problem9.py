#
# Project Euler Problem 9
#
'''
a + b + c = 1000
a^2 + b^2 = c^2
a < b < c

c = 1000 - (a + b)
So then

a^2 + b^2 = (1000 - (a + b))^2

b = 1000 * (a - 500)/(a - 1000)

So now the problem is to find integer solutions of this where a < b, which should be
the first integer solution

'''

import time
import numpy as np

def compute():
    for i in range(1,1000):
        j = float(i)
        val = (2000*j - 1000000)/(2*j - 2000)
        if (val - np.floor(val)) == 0:
            return int(i*val*(1000 - i - val))

def brute_force(n = 1000):
    for a in range(1, n+1):
        for b in range(a + 1, n+1):
            c = n - a - b
            if np.abs(a**2 + b**2 - c**2) < 10**-8:
                return str(a*b*c)
                
            

if __name__ == "__main__":
    start = time.clock()
    print compute()
    print time.clock() - start

    start = time.clock()
    print brute_force(1000)
    print time.clock() - start
