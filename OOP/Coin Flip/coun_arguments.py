import coin_class

def main():
    # Create an object from the Coin class.
    my_coin = coin_class.Coin()

    print('This side is up:', my_coin.get_sideup())
    
    flip(my_coin)

    print('This side is up:', my_coin.get_sideup())

def flip(coin_obj):
    coin_obj.toss()

main()