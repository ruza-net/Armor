from utils import *


def help():
    clear()

    print(b('How to navigate\n'))

    print(('  You\'ve probably already discovered that you can navigate through pages by pressing key in {}. '
          'You don\'t need to press shift to make it uppercase, case doesn\'t matter.\n\n').format(b('[brackets]')))

    print(b('How to fight\n'))

    print(('  You can use various commands while fighting. Type {} and target number to attack enemy with your weapon. '
           'Attacking with weapon costs durability. If you have hero power, type {} to use it. It will cost mana. '
           'If your hero power requires target, you\'ll be asked to type its number. Your pets can also attack enemies.'
           ' Type {}, pet number, and finally, enemy number to have your pet attacking the enemy.\n\n').format(
        b('[A]'),
        b('[H]'),
        b('[P]')
    ))

    o('B', 'Back')

    prompt()
