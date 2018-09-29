"""
Change Return Program -
1. The user enters a cost and then the amount of money given. 
2. The program will figure out the change
3. the number of quarters, dimes, nickels, pennies needed for the change.
because of #2, we assume that the customer will round a dollar up from the price
ie: 
owe 1.28
give 2.00
change 0.72
"""

import math

# 1 entered cost and amount money giver
cost = float(input('How much does this item cost today? '))
given = float(input('How much money will you be paying? '))

# 2 calculating the amount of change
change = given - cost
change_rounded = float("%.2f" % change)
original_change = change_rounded
lst_change = {}

# 3 calculating how many quarters or whatever
if change_rounded/0.25 >= 1:
    no_quarters = (math.floor(change_rounded / 0.25))
    change = change - (no_quarters * 0.25)
    change_rounded = float("%.2f" % change)
    lst_change['quarters'] = no_quarters

if change_rounded / 0.10 >= 1:
    no_dimes = (math.floor(change_rounded / 0.10))
    change = change - (no_dimes * 0.10)
    change_rounded = float("%.2f" % change)
    lst_change['dimes'] = no_dimes

if change_rounded / 0.05 >= 1:
    no_nickels = (math.floor(change_rounded / 0.05))
    change = change - (no_nickels * 0.05)
    change_rounded = float("%.2f" % change)
    lst_change['nickels'] = no_nickels

if change_rounded / 0.01 >= 1:
    no_pennies = (math.floor(change_rounded / 0.01))
    change = change - (no_pennies * 0.01)
    change_rounded = float("%.2f" % change)
    lst_change['pennies'] = no_pennies

print(f'The following is your change for a total amount of ${original_change}')

for key, value in lst_change.items():
    print(f'{value} {key}')