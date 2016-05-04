import sys
from subprocess import call

while True:
    try:
        command = input("> ")
    except EOFError:
        print("\nBye~")
        sys.exit(0)
    call(command.split())
