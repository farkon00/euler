"""
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

res = 0
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        val = i * j
        if str(val) == str(val)[::-1] and val > res:
            res = val

print(res)