def is_multiple(x,y):
    '''is_multiple(x,y) -> bool
    returns True is x is a multiple of y, False otherwise'''
    # check if y divides evenly into x
    return (x % y == 0)

def is_prime(n):
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime'''
    # check every divisor from 2 up to sqrt(n)
    for div in range(2,int(n**0.5)+1):
        if is_multiple(n,div):
            return False  # n isn't prime
    if n == 1:
        return False
    return True  # n is prime

total = 0
number = 2
x = 1

num = int(input('Please enter the number of primes you would like to add:'))

while x <= num:
    if is_prime(number):
        x += 1
        total += number
    number += 1
print(total)
