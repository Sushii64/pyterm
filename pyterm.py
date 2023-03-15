import os
import time
import random
from datetime import datetime as d
import pyfiglet

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

clearscreen()

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

clearscreen()

version = '1.3'
versionName = 'The Rewrite'
helpCommand = '''
    quit - Quits the terminal.
    help - Shows this message.
    whoami - Prints your username.
    clear (cls) - Clears the screen.
    ver - Prints the current version.
    echo - Repeats what you tell it to.
    figlet - Makes ASCII art of text.
'''
helpList = {
    'quit': '''\n    quit - Quits the terminal.\n    Usage: quit\n''',
    'help': '''\n    help - Shows the help message.\n    Usage: help [command]\n''',
    'whoami': '''\n    whoami - Prints your username.\n    Usage: whoami\n''',
    'clear': '''\n    clear - Clears the screen.\n    Usage: clear (or cls)\n''',
    'cls': '''\n    cls - Clears the screen.\n    Usage: cls (or clear)\n''',
    'ver': '''\n    ver - Prints the current version.\n    Usage: ver\n''',
    'echo': '''\n    echo - Repeats what you tell it to.\n    Usage: echo [arg] [string]\n    Arguments: -u - Uppercase.\n''',
    'figlet': '''\n    figlet - Makes ASCII art of text.\n    Usage: figlet [string]'''
}

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
            else:
                text = prompt.split('echo ')[1].strip()
            print(text)
        except IndexError:
            print('Missing argument for echo command.')

    
    def figlet(arg):
        pyfiglet.print_figlet(arg)

commandList = {
    'quit': commands.kill,
    'help': commands.helpme,
    'whoami': commands.whoami,
    'clear': commands.clear,
    'cls': commands.clear,
    'ver': commands.version,
    'echo': commands.echo,
    'figlet': commands.figlet
}

power = 'on'
while power == 'on':
    try:
        prompt = input(f'{username}@pyterm:~$ ')
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