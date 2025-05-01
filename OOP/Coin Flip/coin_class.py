import random

class Coin:
    def __init__(self):
        """Initializes the coin with 'Heads' as the default side up."""
        self.sideup = 'Heads' #sideup is an attribute of Coin class, self is a reference to the object, Heads is the value of sideup

    def toss(self):
        """Flips the coin randomly to either 'Heads' or 'Tails'."""
        self.sideup = 'Heads' if random.randint(0, 1) == 0 else 'Tails'

    def get_sideup(self):
        """Returns the current side up of the coin."""
        return self.sideup

# def main():
#     """Creates a Coin object, displays its initial state, flips it, and displays the new state."""
#     my_coin = Coin()
#     print('This side is up:', my_coin.get_sideup())

#     print('I am tossing the coin ...')
#     my_coin.toss()

#     print('This side is up:', my_coin.get_sideup())

# # Run the program
# main()
