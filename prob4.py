'''
Link: https://projecteuler.net/problem=4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
largest = 0
for i in range(999,100,-1):
    for j in range(i, 100, -1):
        trial = i*j
        string = str(trial)
        if (string[:3] == string[3:][::-1]) and (trial > largest):
            largest = trial

print("largest palindrome is ", largest)
