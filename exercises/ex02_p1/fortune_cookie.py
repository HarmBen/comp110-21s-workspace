"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730368084"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    x: int = randint(1, 4)
    if (x == 1):
        return('You are going to ace COMP110!')
    else:
        if (x == 2):
            return('You earned $100 at CAVA!')
        else:
            if (x == 3):
                return('You will be super happy tomorrow!')
            else:
                return('Unfortunately, you get only get to eat soup next week.')


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
