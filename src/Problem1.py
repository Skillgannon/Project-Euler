#
# Project Euler Problem 1
# Analytic Solution
# y_n = (n) * (1/2) * (floor((x-1)/n)) * (floor((x-1)/n) + 1)
# Is the sum of all numbers less than x, which are divisble by n
# The sum of all numbers divisible by 3 and 5 is then
# y_3 + y_5 - y_15
# The y_15 factor removes one copy of all numbers that are divisible by both 3 and 5
#

from numpy import floor

def analytic(x = 1000, n = 3):
    return n*0.5*floor((x - 1) / n)*(floor((x-1)/n) + 1)


def compute(n = 1000):
    ans = sum(x for x in range(n) if (x % 3 == 0 or x % 5 == 0))
    return ans

if __name__ == "__main__":
    print compute(1000)
    print int(analytic(1000,3) + analytic(1000,5) - analytic(1000,15))
