'''
Link: https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.



'''
for i in range(999, 1, -1):
    for j in range(i, 1, -1):
        for k in range(j, 1, -1):
            if (i+j+k == 1000) and (k**2 + j**2 - i**2 == 0):
                print("Found values: ", i, j, k)
                print("Product", i*j*k)
                exit(0)


