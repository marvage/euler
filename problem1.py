#Solution to Euler Problem 1 in Python 2.7 (https://projecteuler.net/)
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
#my solution - generate the range of both multiples, throw out the duplicates using set then print the sum

a = range(0, 1000, 5)
b = range (0, 1000, 3)
c = set(a + b)
print sum (c)
