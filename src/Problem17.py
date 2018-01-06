# Project Euler Problem 17
#
# Counting the number of letters used to spell out all the numbers
# in the range (1,n)
#
# Can count the letters exactly. 

def translate(n):
    if 0 <= n < 20:
        return singles[n]
    elif n < 1e2:
        return doubles[int(n // 10)] + (singles[n % 10] if (n % 10 != 0) else 0)
    elif n < 1e3:
        # 7 for "hundred", 3 letters for "and"
        return singles[int(n // 100)] + 7 + ((3 + translate(int(n % 1e2))) if (n % 1e2 != 0) else 0)
    elif n < 1e6 :
        # 8 letters for "thousand"
        return translate(int(n // 1e3)) + 8 + (translate(int(n % 1e3)) if (n % 1e3 != 0) else 0)
    else:
        raise ValueError()

def compute(n):
    return sum(translate(i) for i in range(1,n))


singles_set = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

singles = [len(i) for i in singles_set]

doubles_set = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

doubles = [len(i) for i in doubles_set]

if __name__ == "__main__":
    print compute(1001)
