from utils import *
from help import help
from options import options


game = None


while True:
    clear()

    print(b('Welcome to ' + u('Armor') + ', a text-based adventure game!\n'))

    o('P', 'Play adventure')
    o('A', 'Play arena\n')

    o('I', 'Open inventory\n')

    o('O', 'Options')
    o('H', 'How to play\n')

    o('Q', 'Quit')

    option = prompt()

    if option == 'Q':
        clear()

        print(b('Thanks for playing my game, cheers from Jan Růžička!'))

        print('\n' * 4)

        exit(0)

    elif option == 'H':
        help()

    elif option == 'O':
        game = options(game)

        clear()

        if game is not None:
            print(c(i('Game imported successfully!\n\n'), 'yellow'))

            o('O', 'OK')

            prompt()
