#
# Project Euler Problem 15
#
# Traversing an n x n grid
#
# This problem involves starting at the top left corner of an n x n grid,
# and traversing either down or to the right until the bottom right corner has
# been reached.
#
# Traversing an n x n grid in this fashion involves n motions to the right,
# and n motions down. The aim is to account for all unique traversals following
# these rules.
#
# This problem can be solved exactly using combinatorics -
# there are two 2N choose N moves, thus making the total set
# f(N) = (2N)!/ (N! * (2N - N)!) = (2N)! / (N!)^2


import time
import numpy as np

def binomial(n,k):
    # Calculating binomial coefficients

    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))

def compute(n):
    # Shorthand for this specific problem

    return np.math.factorial(2*n) / (np.math.factorial(n))**2
        
        
            

if __name__ == "__main__":
    # Verification - result should be 6
    print binomial(4,2)
    print compute(2)

    # Testing
    print compute(20)
