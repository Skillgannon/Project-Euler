#
# Project Euler Problem 14
#
# Finding the largest Collatz sequence below a threshold value
#
# A collatz sequence is one where n -> n/2 (if n == even) or n -> 3n+1 (if n == odd)
# The sequence involves integer progressions, and should (although there is no definitive proof)
# converge to 1.
#
# Two solutions are presented - one which simply brute forces the length of all sequences below a threshold
# value; the second uses memoization. This significantly decreases the run time
# at the cost of increasing the memory cost of the process.
# The memoization implemented here works for thresholds of 10 million, but runs into memory overflows when testing with values less than 100 million
# However, the memoization process can be improved by minimizing the number of points that need to be stored, as the Collatz sequence is a 1:1 process


import time
import numpy as np
import operator

def collatz_step(n):
    # Calculating one step of the Collatz chain
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1

    return n

def compute(threshold):
    # Stores all calculated values in a dict for memoization purposes
    struc = {}
    struc[1] = 1

    threshold = int(threshold)

    # Starting at the highest value and working backwards, as starting at the
    # upper end means that there will more likely be overlap in values,
    # increasing the efficacy of the memozation process
    for n in xrange(threshold,0,-1):
        n_i = n

        # Tests if a Collatz chain has already passed through this point
        if n not in struc:
            state = 1

        # Stores a chain starting from a defined point. All values in the chain
        # (until it reaches a point where a chain has already passed through)
        n_set = []
        n_set.append(n_i)

        # Iterates through chain
        while state:
            n_i = collatz_step(n_i)
            n_set.append(n_i)
            if n_i in struc:
                state = 0

        # Constructs a vector corresponding to the length of the Collatz chains of all
        # points along its progression
        n_length = np.arange(struc[n_i], len(n_set) + struc[n_i])[::-1]

        for i in xrange(len(n_set) - 1):
            struc[n_set[i]] = n_length[i]

    max_val = 0
    max_loc = 0

    # Searches for the largest chain under the threshold
    # This process must be used to filter out chains larger than the specificed threshold (as chains can pass through these values)
    # Technically this should be spuerflous, because any chain starting at n_1 > threshold
    # that has been calculated, must have been reached by starting at n_2 < threshold, where the length of
    # n_2 > n_1.
    # However this search is still used rather than one of the more efficient inbuilt max searches for dicts
    # because as threshold scales larger than 1e6 (the value used in this problem) there will be significantly more points
    # in the calculated set above the threshold value. As such, filtering out those becomes more critical

    for i in xrange(1, threshold + 1):
        temp = struc[i]
        if temp > max_val:
            max_val, max_loc = temp, i

    return max_loc

def brute_force(threshold):
    threshold = int(threshold)
    
    max_val = 0
    max_loc = 0
    for n in xrange(threshold,0,-1):
        n_i = n
        n_length = 1
        
        while n_i > 1:
            n_i = collatz_step(n_i)
            
            n_length += 1

        if n_length > max_val:
            max_val, max_loc = n_length, n

    return max_loc
            
        
        
            

if __name__ == "__main__":
    start = time.clock()
    print compute(1e6)
    print time.clock() - start

    start = time.clock()
    print brute_force(1e6)
    print time.clock() - start
