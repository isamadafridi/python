import coin_class

def main():
    """Creates a Coin object, displays its initial state, flips it, and displays the new state."""
    my_coin = coin_class.Coin()
    print('This side is up:', my_coin.get_sideup())

    print('I am tossing the coin ...')
    my_coin.toss()

    print('This side is up:', my_coin.get_sideup())

# Run the program
main()