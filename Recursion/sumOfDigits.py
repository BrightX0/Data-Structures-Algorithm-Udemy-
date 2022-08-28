# The aims Of this Py was to Solve or crack the interview Question
# on how to find the sum of digits of a positive integer number using recursion

def sumofDigits(n):
    assert n >= 0 and int(n) == n, 'Only Positive Integer are Allowed!!!'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumofDigits(int(n/10))


print(sumofDigits(4545))
