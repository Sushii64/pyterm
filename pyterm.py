import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

username = input('Enter your username: ')

os.system('cls' if os.name == 'nt' else 'clear')

def terminal():
    looping = True
    version = 'v1.0'
    versionName = 'The First One'
    helpCommand = '''
    quit - Quits the terminal.
    help - Shows this message.
    whoami - Prints your username.
    clear (cls) - Clears the screen.
    ver - Prints the current version.
    installer - Shows an installer prompt.
    '''
    availablePackages = '''
    Available Packages:
    -------------------
    pix
    blankpkg
    '''
    installedPix = False
    installedBlankPKG = False
    while looping:
        prompt = input('\u001b[37m' + str(username) + '@pyterm:~$ ')
        if prompt == 'quit':
            quit()
        elif prompt == 'help':
            print('\u001b[0m' + str(helpCommand))
            continue
        elif prompt == 'whoami':
            print('\u001b[0m' + str(username))
            continue
        elif prompt == 'clear' or prompt == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif prompt == 'ver':
            print('\u001b[0mPyTerm ' + str(version) + '\n"' + str(versionName) + '"')
            continue
        elif prompt == 'installer':
            installPrompt = input('\u001b[37m' + str(username) + '@pyterm.Installer >>> ')
            if installPrompt == 'pix':
                print('\u001b[0mInstalling package "pix"...')
                time.sleep(1)
                installedPix = True
                continue
            elif installPrompt == 'blankpkg':
                print('\u001b[0mInstalling package "blankpkg"...')
                time.sleep(.5)
                installedBlankPKG = True
                continue
            elif installPrompt == 'list':
                print('\u001b[0m' + str(availablePackages))
                continue
            else:
                print('\u001b[31mPackage "' + str(installPrompt) + '" not found.')
                continue
        elif prompt == 'pix':
            if installedPix:
                print('-----------\n|         |\n|  |   |  |\n| -_____- |\n|         |\n-----------')
                continue
            else:
                print('\u001b[31mCommand "pix" not found.')
                continue
        elif prompt == 'blankpkg':
            if installedBlankPKG:
                continue
            else:
                print('\u001b[31mCommand "blankpkg" not found.')
                continue
        else:
            print('\u001b[31mCommand "' + str(prompt) + '" not found.')
            continue

terminal()
