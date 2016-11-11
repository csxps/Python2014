# this program calculates the total bill for a restaurant patron

# set cost of each dish in dollars
appetizer = 8.00
entree = 15.00
dessert = 5.00

subtotal = appetizer + entree + dessert # total cost of food
tax = 0.08 * subtotal                   # tax on food
tip = 2 * tax + 1.00                    # compute tip from tax

total = subtotal + tax + tip            # calculate entire bill

print(total)                            # display result to user
