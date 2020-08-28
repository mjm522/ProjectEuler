'''
Link: https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Link: https://projectile.net/problem=6

'''

N=100
sum_first_100_natural_numbers = (N/2)*(N+1)
sum_first_100_natural_numbers_square = sum_first_100_natural_numbers**2
sum_first_100_square_natural_numbers_square = (N/6)*(2*N+1)*(N+1)

print(sum_first_100_natural_numbers_square-sum_first_100_square_natural_numbers_square)