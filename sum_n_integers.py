x = int(input('Please enter the number of consecutive positive integers you would like to add:'))

def sum_of_integers(n):
    '''adds the first n positive integers'''
    total = 0            # initialize the total at 0
    currentNumber = 1    # this keeps track of the next number to add
    while (currentNumber <= n):
        total += currentNumber       # add the current number to our total
        currentNumber += 1   # go to the next number
    return total  # output the answer

print(sum_of_integers(x))
