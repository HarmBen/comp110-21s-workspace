"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730368084"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print('Your fortune cookie says...')

fortune = randint(1, 4)

if (fortune == 1):
    print('You are going to ace COMP110!')
else:
    if (fortune == 2):
        print('You earned $100 at CAVA!')
    else:
        if (fortune == 3):
            print('You will be super happy tomorrow!')
        else:
            print('Unfortunately, you get only get to eat soup next week.')

print("Now, go spread positive vibes!")