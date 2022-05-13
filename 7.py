"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

i = 2
primes = []
while len(primes) < 10001:
    for j in primes:
        if i % j == 0:
            break
    else:
        primes.append(i)
    i += 1

print(primes[-1])