import os
import time
import random
from datetime import datetime as d
import pyfiglet
import colorama
from colorama import Fore

version = '1.6'
versionName = 'Package Party 2'
Cn = 'pyterm'

def clearscreen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

clearscreen()

print(f'''
 ____       _____                   
|  _ \ _   |_   _|__ _ __ _ __ ___  
| |_) | | | || |/ _ \ '__| '_ ` _ \ 
|  __/| |_| || |  __/ |  | | | | | |
|_|    \__, ||_|\___|_|  |_| |_| |_|
       |___/                        
Version {version}: "{versionName}"
'''
)

try:
    I = input('[L]ogin, [O]ptions, or [Q]uit ')
except KeyboardInterrupt:
    print('\nAbort.')
    quit()

if I == 'L' or I == 'l':
    try:
        username = input('Enter your username: ')
    except KeyboardInterrupt:
        print('\nAbort.')
        quit()
elif I == 'Q' or I == 'q':
    try:
        print('Abort.')
        quit()
    except KeyboardInterrupt:
        print('\nAbort.')
        quit()
else:
    try:
        O = input('Options\n--------\n[T]erminal Color\n[L]icense\n"[C]omputer" Name\n')
        if O == 'T' or O == 't':
            Ch = input('Colors\n--------\n[D]efault\n[W]hite\n[R]ed\n[Y]ellow\n[G]reen\n[B]lue\n[C]yan\n[M]agenta\n')
            if Ch == 'D' or Ch == 'd':
                print(Fore.RESET)
                print('Color set.')
            elif Ch == 'W' or Ch == 'w':
                print(Fore.WHITE)
                print('Color set.')
            elif Ch == 'R' or Ch == 'r':
                print(Fore.RED)
                print('Color set.')
            elif Ch == 'Y' or Ch == 'y':
                print(Fore.YELLOW)
                print('Color set.')
            elif Ch == 'G' or Ch == 'g':
                print(Fore.GREEN)
                print('Color set.')
            elif Ch == 'B' or Ch == 'b':
                print(Fore.BLUE)
                print('Color set.')
            elif Ch == 'C' or Ch == 'c':
                print(Fore.CYAN)
                print('Color set.')
            elif Ch == 'M' or Ch == 'm':
                print(Fore.MAGENTA)
                print('Color set.')
            else:
                print(Fore.RESET)
                print('Defaulting.')
        elif O == 'L' or O == 'l':
            Li = open("LICENSE", "r")
            print(Li.read())
            Li.close()
        elif O == 'C' or O == 'c':
            Cn = input('\nusername@pyterm\n\nWhat do you want to change "pyterm" to?\n')
            print(f'"Computer" name set as "{Cn}"\n')
        time.sleep(0.05)
        print('Saving...')
        time.sleep(0.2)
        try:
            username = input('Enter your username: ')
        except KeyboardInterrupt:
            print('\nAbort.')
            quit()
    except KeyboardInterrupt:
        print('\nAbort.')
        quit()

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

clearscreen()

helpCommand = '''
    quit - Quits the terminal.
    help - Shows this message.
    whoami - Prints your username.
    clear (cls) - Clears the screen.
    ver - Prints the current version.
    echo - Repeats what you tell it to.
    parcel - Installs new packages to use.
'''
helpList = {
    'quit': '''\n    quit - Quits the terminal.\n    Usage: quit\n''',
    'help': '''\n    help - Shows the help message.\n    Usage: help [command]\n''',
    'whoami': '''\n    whoami - Prints your username.\n    Usage: whoami\n''',
    'clear': '''\n    clear - Clears the screen.\n    Usage: clear (or cls)\n''',
    'cls': '''\n    cls - Clears the screen.\n    Usage: cls (or clear)\n''',
    'ver': '''\n    ver - Prints the current version.\n    Usage: ver\n''',
    'echo': '''\n    echo - Repeats what you tell it to.\n    Usage: echo [arg] [string]\n    Arguments:\n    -u - Uppercase.\n    -l - Lowercase.\n    -sc - Swap case.\n    -r - Reversed.\n    -se - Seperate letters\n''',
    'parcel': '''\n    parcel - Installs new packages to use.\n    Usage: parcel [arg] [package]\n    Use "parcel help" to see all the usable arguments\n'''
}

class package:
    def figlet(arg):
        pyfiglet.print_figlet(arg)
    
    def ball(arg):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

        answer = random.choice(responses)
        if not arg == '':
            print(arg)
        print("My answer is:", answer)

class commands:
    def kill(arg):
        quit()

    def helpme(arg):
        if arg in helpList:
            print(helpList.get(arg))
        else:
            print(helpCommand)

    def whoami(arg):
        print(username)
    
    def clear(arg):
        clearscreen()
    
    def version(arg):
        print(f'\n    PyTerm v{version}\n    "{versionName}"\n')
    
    def echo(arg):
        try:
            if '-u' in prompt:
                text = prompt.split('-u')[1].strip().upper()
            elif '-l' in prompt:
                text = prompt.split('-l')[1].strip().lower()
            elif '-sc' in prompt:
                text = prompt.split('-sc')[1].strip().swapcase()
            elif '-r' in prompt:
                text = prompt.split('-r')[1].strip()[::-1]
            elif '-se' in prompt: 
                textB = prompt.split('-se')[1].strip()
                textL = [*textB]
                text = ' '.join(textL)
            else:
                text = prompt.split('echo ')[1].strip()
            print(text)
        except IndexError:
            print('Missing argument for echo command.')
    
    def cfiglet(arg):
        if 'fig' in installed:
            package.figlet(arg)
        else:
            print('Command "fig" not found.')
    
    def cball(arg):
        if '8ball' in installed:
            package.ball(arg)
        else:
            print('Command "8ball" not found.')

    def package(arg):
        try:
            if 'help' in prompt:
                reply = '\n    PkgMaster v1.0\n    -----------\n    help - Shows this message.\n    get - Installs a package.\n    remove - Removes a package.\n    list\n        -a - Lists the available packages.\n        -i - Lists the installed packages.\n'
            elif 'get' in prompt:
                argu = prompt.split('get')[1].strip()
                if not argu == '':
                    if argu in pkgList:
                        reply = f'Installing package "{argu}"'
                        installPackage(argu)
                        time.sleep(0.2)
                    else:
                        reply = f'Incorrect package "{argu}"'
                else:
                    reply = 'Missing package name.'
            elif 'remove' in prompt:
                argu = prompt.split('remove')[1].strip()
                if not argu == '':
                    if argu in installed:
                        reply = f'Uninstalling package "{argu}"'
                        rmpkg(argu)
                        time.sleep(0.2)
                    else:
                        reply = f'Incorrect package "{argu}"'
                else:
                    reply = 'Missing package name.'
            elif 'list -i' in prompt:
                reply = " ".join(installed)
            elif 'list -a' in prompt:
                reply = " ".join(pkgList)
            else:
                reply = 'Incorrect argument. Use "parcel help".'
            print(reply)
        except IndexError:
            print('Missing argument for parcel command.')

pkgList = [
    'fig',
    '8ball'
]

installed = [
]

def installPackage(pkg):
    if pkg in pkgList:
        installed.append(pkg)
        pkgList.remove(pkg)

def rmpkg(pkg):
    if pkg in installed:
        installed.remove(pkg)
        pkgList.append(pkg)

commandList = {
    'quit': commands.kill,
    'help': commands.helpme,
    'whoami': commands.whoami,
    'clear': commands.clear,
    'cls': commands.clear,
    'ver': commands.version,
    'echo': commands.echo,
    'parcel': commands.package,
    'fig': commands.cfiglet,
    '8ball': commands.cball
}

power = 'on'
while power == 'on':
    try:
        prompt = input(f'{username}@{Cn}:~$ ')
        if prompt.split():
            commandInput = prompt.split()
            command = commandInput[0]
            if len(commandInput) > 1:
                arg = ' '.join(commandInput[1:])
            else:
                arg = ''
            if command in commandList:
                commandList[command](arg)
            else:
                print(f'Command "{command}" not found.')
    except KeyboardInterrupt:
        print ('')
        continue
