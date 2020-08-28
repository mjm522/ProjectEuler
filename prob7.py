'''
Link: https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?



'''

def is_prime(inp):
    return all(inp % i for i in range(2, inp))

N=10001
n = 0
counter = 1

while n != N:
    counter += 1
    if is_prime(counter):
        n += 1
print(counter)
