'''


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.



'''



def is_prime(inp):
    return all(inp % i for i in range(2, inp))

N = 2000000

N = 10

numbers = range(2, N)

for n in numbers:
    


# sum_ = 0

# for i in range(N, 2, -1):
#     if is_prime(i):
#         sum_+= i

# print("Sum is", sum_)