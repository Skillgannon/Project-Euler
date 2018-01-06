#
# Project Euler Problem 3
# Analytic approach
# Any number n can be partitioned so that
# n = \sum_{i=0}^{m} p_{i}, where p is a non-unique set of prime numbers,
# which are all factors of n.

# Numerical approach
#  - Find the smallest prime factor of n
#  - Find n_p = n / p_{0}, set that n = n_p
#  - Repeat until n is a prime number
# To find the smallest prime factor
#  - Find the smallest number that will cleanly divide by n, this number must be prime


import numpy as np

def smallest_factor(n, threshold = 2):
    # Threshold factor removes the need to search over small numbers that have previously been searched over for  a prior prime
    assert n >= 2
    for i in range(threshold, int(np.sqrt(n) + 1)): # The largest factor will either be n, or < sqrrt(n)
        if n % i == 0:
            return i
    return n


def compute(n = 1000):
    while True:
        p = smallest_factor(n)
        if p < n:
            n //= p
        else:
            return n
            

if __name__ == "__main__":
    print compute(600851475143)
