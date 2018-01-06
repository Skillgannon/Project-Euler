#
# Project Euler Problem 2
# Analytic Solution
# No compact solution
#
# Numerical solution
# Summation

from numpy import floor

def analytic(x = 1000, n = 3):
    return n*0.5*floor((x - 1) / n)*(floor((x-1)/n) + 1)


def compute(n = 1000):
    net = 0
    a_1 = 1
    a_2 = 2
    while a_1 <= n:
        if a_1 % 2 == 0: # Tests for if a_1 is even
            net += a_1
        a_1, a_2 = a_2, a_1 + a_2
    return(net)
            

if __name__ == "__main__":
    print compute(4000000)
