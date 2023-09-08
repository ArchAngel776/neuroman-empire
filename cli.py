from sys import argv
from commands import commands


if len(argv) < 1:
    print("No command selected")
    exit(-1)

name, args = argv[1], argv[2:]

Command = commands().get(name)
command = Command()

command.run(*args)
