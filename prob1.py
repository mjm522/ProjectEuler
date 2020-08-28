"""
Link: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def highest_divisible(N, divisor, including=True):
    if not including:
        N = N-1
    while N != 0:
        if N%divisor==0:
            break
        else:
            N -= 1
    return N

n = 1000
highest_3 = highest_divisible(n, 3, False)
highest_5 = highest_divisible(n, 5, False)
highest_15 = highest_divisible(n, 15, False)

sum_3 = (highest_3/6)*(highest_3 + 3)
sum_5 = (highest_5/10)*(highest_5 + 5)
sum_15 = (highest_15/30)*(highest_15 + 15)

print(sum_3 + sum_5 - sum_15)
