# Project Euler Problem 20
#
# Calculating the sum of all integers in the number n!
# Can be calculated directly as a result of Pythons arbitrary precision arithmatic


import numpy as np

def compute(n):
    # Calculates n!, converts it to a string, isolates each character of that string
    # and then sums the integer form of them
    return sum(int(i) for i in str(np.math.factorial(n)))

if __name__ == "__main__":
    print compute(100)
