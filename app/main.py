import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) == 3 and commands[0] == "mv":

        #with open(commands[1]) as file_to_read:

