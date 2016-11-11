def is_multiple(x,y):
    '''is_multiple(x,y) -> bool
    returns True is x is a multiple of y, False otherwise'''
    # check if y divides evenly into x
    if (x % y == 0):
        print(y)

def sum_of_proper_divs(n):
    total = 0
    x = n
    y = 1
    while y != x:
        is_multiple(x, y)
        if (x % y == 0):
            total += y
        y += 1
    return total

print(sum_of_proper_divs(496))
