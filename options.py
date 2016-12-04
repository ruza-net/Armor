from utils import *


def options(game):
    while True:
        clear()

        print(b('Options\n'))

        o('S', 'Save the game')
        o('O', 'Open saved game\n')

        o('B', 'Back')

        option = prompt()

        if option == 'B':
            return

        elif option == 'S':
            while True:
                clear()

                where = input('Where do you want the file save to ({} for default)? '.format(i('default')))

                if where == 'default':
                    file = proj_dir

                    if not os.path.isdir(file):
                        os.mkdir(file)
                        os.chmod(file, os.st.S_IWRITE)

                else:
                    if not os.path.isdir(where):
                        print(e('Path doesn\'t exist: {}'.format(where)))

                        continue

                    file = where

                name = input('What\'s the name of your snapshot ({} for default)? '.format(i('default')))

                with open(file + '/' + name, 'w+') as f:
                    write_snapshot(f, game)

                clear()

                print(c(i('Snapshot has been written successfully!\n\n'), 'yellow'))

                o('O', 'OK')

                prompt()

                return game

        elif option == 'O':
            clear()

            where = input('Where is your saved game ({} for default)? '.format(i('default')))

            if where == 'default':
                where = proj_dir

            elif where == 'test':
                with open('sample_snapshot', 'r') as f:
                    return parse_snapshot(f)

            name = input('What\'s the name of your file ({} for default)? '.format(i('default')))

            if os.path.exists(where + '/' + name):
                with open(where + '/' + name, 'r') as f:
                    return parse_snapshot(f)

            else:
                clear()

                print(e('File doesn\'t exist: {}\n\n'.format(where)))

                o('O', 'OK')

                prompt()
