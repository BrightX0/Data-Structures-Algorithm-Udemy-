# Recursion is a function that calls itself multiple times
# until the given condition within the function fails
# when to use Recursion..
# if the problem can be easily be broken into a similar problem
# When using a traverse Tree

def factorial(n):
    assert n>=0 and int(n) == n, 'The Number has to be a Positive Integer'
    if n in [0,1]: return 1
    else: return n * factorial(n-1)


print(factorial(10))