# Project Euler Problem 24
#
# Trying to find the 1 millionth Lexicographic permutation of the numbers {0,1,...,9}
# Solution found using combinatronics. For example, there are 2*(9!) numbers
# covering 0XXXXXXXXX and 1XXXXXXXXX. However, 3*(9!) is greater than 1 million
# So the number should be of the form 2XXXXXXXXX.
# This logic can be followed to solve for all 10 digits. 

import numpy as np

def return_set(n,l):
    # Inputs:
    # n - the upper limit, in this case 1 million
    # l - the upper limit of the numbers that can be used to
    # construct the lexiographic permutations - in this case the set {0,1,...,l}
    out = []
    # Uses combinatorics to find the set of numbers that does not go above 1 million
    for i in xrange(0,l + 1):
        factor = np.math.factorial(l-i)
        temp = int(np.floor(n / np.float(factor)))
        out.append(temp)
        n = n - temp*factor

    # The answers for the above loop do not count for the elimination of variables
    # This loop then translates to take into account the elimination of variables
    numbers = np.arange(0,l + 1)
    out_set = []
    for i in out:
        out_set.append(numbers[i])
        numbers = np.delete(numbers,i)
        
    return "".join([str(i) for i in out_set])


print return_set(1e6,9)
        
    
