import os
import time
import random
from datetime import datetime as d

os.system('cls' if os.name == 'nt' else 'clear')

username = input('Enter your username: ')

root = False

if username == 'root':
    repeating = True
    while repeating:
        passwd = input('Enter password for root: ')
        if passwd == 'root':
            root = True
            break
        else:
            print('Incorrect password.')
            continue

os.system('cls' if os.name == 'nt' else 'clear')

def terminal():
    powerON = True
    version = 'v1.2'
    versionName = 'Minor Modifications'
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
    madlibs
    '''
    installedPix = False
    installedBlankPKG = False
    installedPIOS = False
    installedEightBall = False
    installedVersionGen = False
    installedMadLibs = False
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
                if installedPix:
                    print('\u001b[0mpix is already installed.')
                else:
                    print('\u001b[0mInstalling package "pix"...')
                    time.sleep(1)
                    installedPix = True
                continue
            elif installPrompt == 'blankpkg':
                if installedBlankPKG:
                    print('\u001b[0mblankpkg is already installed.')
                else:
                    print('\u001b[0mInstalling package "blankpkg"...')
                    time.sleep(.5)
                    installedBlankPKG = True
                continue
            elif installPrompt == 'pios':
                if installedPIOS:
                    print('\u001b[0mpios is already installed.')
                else:
                    print('\u001b[0mInstalling package "pios"...')
                    time.sleep(2)
                    installedPIOS = True
                continue
            elif installPrompt == 'eightball':
                if installedEightBall:
                    print('\u001b[0meightball is already installed.')
                else:
                    print('\u001b[0mInstalling package "eightball"...')
                    time.sleep(3)
                    installedEightBall = True
                continue
            elif installPrompt == 'versiongen':
                if installedVersionGen:
                    print('\u001b[0mversiongen is already installed.')
                else:
                    print('\u001b[0mInstalling package "versiongen"...')
                    time.sleep(2)
                    installedVersionGen = True
                continue
            elif installPrompt == 'madlibs':
                if installedMadLibs:
                    print('\u001b[0mmadlibs is already installed.')
                else:
                    print('\u001b[0mInstalling package "madlibs"...')
                    time.sleep(1)
                    installedMadLibs = True
            elif installPrompt == 'list':
                print(f'\u001b[0m{availablePackages}')
                continue
            elif installPrompt == '*':
                yn = input('\u001b[0mAre you sure you want to install every package? [Y/N] ')
                if yn == 'Y' or yn == 'y':
                    if installedPix:
                        print('\u001b[0mpix is already installed.')
                        time.sleep(.1)
                    else:
                        print('\u001b[0mInstalling package "pix"...')
                        time.sleep(1)
                    installedPix = True
                    if installedBlankPKG:
                        print('\u001b[0mblankpkg is already installed.')
                        time.sleep(.1)
                    else:
                        print('\u001b[0mInstalling package "blankpkg"...')
                        time.sleep(.5)
                        installedBlankPKG = True
                    if installedPIOS:
                        print('\u001b[0mpios is already installed.')
                        time.sleep(.1)
                    else:
                        print('\u001b[0mInstalling package "pios"...')
                        time.sleep(2)
                        installedPIOS = True
                    if installedEightBall:
                        print('\u001b[0meightball is already installed.')
                        time.sleep(.1)
                    else:
                        print('\u001b[0mInstalling package "eightball"...')
                        time.sleep(3)
                        installedEightBall = True
                    if installedVersionGen:
                        print('\u001b[0mversiongen is already installed.')
                        time.sleep(.1)
                    else:
                        print('\u001b[0mInstalling package "versiongen"...')
                        time.sleep(2)
                        installedVersionGen = True
                    if installedMadLibs:
                        print('\u001b[0mmadlibs is already installed.')
                    else:
                        print('\u001b[0mInstalling package "madlibs"...')
                        time.sleep(1)
                        installedMadLibs = True
                    continue
                else:
                    print('\u001b[0mAbort.')
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
                question = input('\u001b[0mAsk your question: ')

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
                answer = input('\u001b[0mSelect a style: [S]eperated [C]ombined ')

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
        elif prompt == 'madlibs':
            if installedMadLibs:
                adjective = input('\u001b[0mChoose an adjective: ')
                p_noun = input('Choose a plural noun: ')
                noun = input('Choose a noun: ')
                place = input('Name a place: ')
                adjective2 = input('Choose an adjective: ')
                noun2 = input('Choose a noun: ')

                print('------------------------------------------')
                print('Be kind to your', adjective, p_noun)
                print('For a duck may be somebody\'s', noun + ',')
                print('Be kind to your', p_noun, 'in', place)
                print('Where the weather is always', adjective2 + '. \n')
                print('You may think that this is the', noun2 + ',')
                print('Well it is.')
                print('------------------------------------------')
                continue
            else:
                print('\u001b[31mCommand "madlibs" not found.')
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
# versionInternal = 'v1.2'
#
# if not versionCheck == versionInternal:
#    print(f'\u001b[31mYou have an outdated version of PyTerm!\nYour version: {versionInternal}\nLatest version: {versionCheck}\nPlease update!')
###

###
#       elif prompt == 'changelog':
#            print(f'\u001b[0m{changelogSource}')
#            continue
###