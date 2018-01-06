#
# Project Euler Problem 4
# Brute force
# - Search through all products of i*j and test to see if it's a palindrome

# Fast approach
# Manually construct palidnromes, look for factors, see if there are 2 factos in the 3 digit numbers

import numpy as np
import time


def brute_force(n,m):
    return max(i * j for i in range(n, m) for j in range(n,m) if str(i*j) == str(i*j)[::-1])


def compute(n = 3):
    # n = number of digits being searched over (so between 10**(n-1) and 10**(n) - 1)
    maxval = (10**n-1)**2 # Largest possible palindrom
    maxfactor = 10**n-1 # Largest possible factor
    minfactor = 10**(n-1) # Smallest possible factor
    factors_list = np.arange(minfactor, maxfactor + 1) # List of all possible factors
    
    for i in maxval - np.arange(maxval - 10**(2*n-1) + 1):
        # Searching from largest possible palindrome to smallest possible palindrome
        temp = str(i)
        if temp == temp[::-1]:
            ix = np.where(i % factors_list == 0)
            if ix[0].size > 1:
                factors = factors_list[ix[0][-2:]] # selects the last 2 elements of the factors list
                if np.abs(np.prod(factors) - i) < 1:
                    return temp
                
                
            

if __name__ == "__main__":
    start = time.clock()
    print brute_force(100,1000)
    print time.clock() - start
    start = time.clock()
    print compute(3)
    print time.clock() - start
