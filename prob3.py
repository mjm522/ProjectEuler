"""
Link: https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

num = 600851475143

def is_prime(inp):
    return all(inp % i for i in xrange(2, inp))


fact = int(num**0.5) + 1

while fact > 0:

    if num%fact == 0:

        if is_prime(fact):
            print "Largest prime factor is \t", fact
            break
        elif is_prime(num/fact):
            print "Largest prime factor is \t", (num/fact)
            break

    fact -= 1


