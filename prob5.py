'''
Link: https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
N = 20

def prime_factors(n):
    prime_facts = []
    for i in range(2, n + 1):
        while n % i == 0:
            prime_facts.append(i)
            n = n / i
        if n == 1:
            break
    return prime_facts

def factors(n):
    facts = [n]
    for i in range(int(n/2), 1, -1):
        if n%i == 0:
            facts.append(i)
    return facts

ap = [prime_factors(k) for k in range(1, N+1)]

unique_facts = []

for fact in ap:
    for f in fact:
        unique_facts += [f for _ in range(fact.count(f)-unique_facts.count(f))]

print("prime factorisation \n", ap)
print("unique factors \n", unique_facts)

p = 1
for j in unique_facts:
    p*=j
print("LCM", p)