import os
import time
import random
from datetime import datetime as d

os.system('cls' if os.name == 'nt' else 'clear')

username = input('Enter your username: ')

os.system('cls' if os.name == 'nt' else 'clear')

def terminal():
    powerON = True
    version = 'v1.1'
    versionName = 'Package Party'
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
    pios
    eightball
    versiongen
    '''
    installedPix = False
    installedBlankPKG = False
    installedPIOS = False
    installedEightBall = False
    installedVersionGen = False
    while powerON:
        prompt = input(f'\u001b[37m{username}@pyterm:~$ ')
        if prompt == 'quit':
            quit()
        elif prompt == 'help':
            print(f'\u001b[0m{helpCommand}')
            continue
        elif prompt == 'whoami':
            print(f'\u001b[0m{username}')
            continue
        elif prompt == 'clear' or prompt == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif prompt == 'ver':
            print(f'\u001b[0mPyTerm {version}\n"{versionName}"')
            continue
        elif prompt == 'installer':
            installPrompt = input(f'\u001b[37m{username}@pyterm.Installer >>> ')
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
            elif installPrompt == 'pios':
                print('\u001b[0mInstalling package "pios"...')
                time.sleep(2)
                installedPIOS = True
                continue
            elif installPrompt == 'eightball':
                print('\u001b[0mInstalling package "eightball"...')
                time.sleep(3)
                installedEightBall = True
                continue
            elif installPrompt == 'versiongen':
                print('\u001b[0mInstalling package "versiongen"...')
                time.sleep(2)
                installedVersionGen = True
                continue
            elif installPrompt == 'list':
                print(f'\u001b[0m{availablePackages}')
                continue
            else:
                print(f'\u001b[31mPackage "{installPrompt}" not found.')
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
        elif prompt == 'pios':
            if installedPIOS:
                sleeptime = 0.05

                def pios():
                    time.sleep(sleeptime)
                    print('\u001b[0m')
                    print('''             88    ,ad8888ba,     ad88888ba ''')
                    time.sleep(sleeptime)
                    print('''             ""   d8"'    `"8b   d8"     "8b''')
                    time.sleep(sleeptime)
                    print('''                 d8'        `8b  Y8,        ''')
                    time.sleep(sleeptime)
                    print('''8b,dPPYba,   88  88          88  `Y8aaaaa,  ''')
                    time.sleep(sleeptime)
                    print('''88P'    "8a  88  88          88    `"""""8b,''')
                    time.sleep(sleeptime)
                    print('''88       d8  88  Y8,        ,8P          `8b''')
                    time.sleep(sleeptime)
                    print('''88b,   ,a8"  88   Y8a.    .a8P   Y8a     a8P''')
                    time.sleep(sleeptime)
                    print('''88`YbbdP"'   88    `"Y8888Y"'     "Y88888P" ''')
                    time.sleep(sleeptime)
                    print('''88                                          ''')
                    time.sleep(sleeptime)
                    print('''88                                          ''')
                    time.sleep(sleeptime)
                    print('''                                            ''')
                    time.sleep(sleeptime)
                    print('''                                            ''')
                    time.sleep(sleeptime)
                    print('''   "operating system of the future (TM)"    ''')

                pios()
                time.sleep(2)
                continue
            else:
                print('\u001b[31mCommand "pios" not found.')
                continue
        elif prompt == 'eightball':
            if installedEightBall:
                question = input('Ask your question: ')

                def eightball(str):
                    options = ['yes', 'no', 'maybe', 'ask again later', 'yes, definitely', 'without a doubt', 'it is certain', 'most likely', 'absolutely not']
                    chosenOption = random.choice(options)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thinking...')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('"' + str + '"' + '\nMy sources say ' + chosenOption)

                eightball(question)
                continue
            else:
                print('\u001b[31mCommand "eightball" not found.')
                continue
        elif prompt == 'versiongen':
            if installedVersionGen:
                os.system('cls' if os.name == 'nt' else 'clear')
                answer = input('Select a style: [S]eperated [C]ombined ')

                t = d.now()
                cdt = t.strftime('%Y%m%d')
                sdt = t.strftime('%Y.%m.%d')
                    
                if answer == 'S' or answer == 's':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(sdt)
                    continue
                elif answer == 'C' or answer == 'c':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cdt)
                    continue
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Error: Not an option')
                    continue
            else:
                print('\u001b[31mCommand "versiongen" not found.')
                continue
        else:
            print(f'\u001b[31mCommand "{prompt}" not found.')
            continue

terminal()

# Unfinished website stuff

###
# from urllib.request import urlopen
#
# changelogSourceURL = 'https://pixsplanet.github.io/pyterm/changelog"'
# changelogSourceRAW = urlopen(changelogSourceURL)
# changelogSourceENCODED = changelogSourceRAW.read()
# changelogSource = changelogSourceENCODED.decode("utf-8")
#
# versionCheckURL = 'https://pixsplanet.github.io/pyterm/version"'
# versionCheckRAW = urlopen(versionCheckURL)
# versionCheckENCODED = versionCheckRAW.read()
# versionCheck = versionCheckENCODED.decode("utf-8")
#
# versionInternal = 'v1.0'
#
# if not versionCheck == versionInternal:
#    print('\u001b[31mYou have an outdated version of PyTerm!\nYour version:' + str(versionInternal) + '\nLatest version:' + str(versionCheck) + '\nPlease update!')
###

###
#       elif prompt == 'changelog':
#            print('\u001b[0m' + str(changelogSource))
#            continue
###