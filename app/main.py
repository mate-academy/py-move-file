import os


def move_file(command: str):
    command_format = command.replace("/", ' ').split()[1:]
    for i in range(len(command_format) - 2):
        os.mkdir("/".join(command_format[1:i + 2]))
    path = "/".join(command_format[1:])
    with open(command_format[0], "r") as current_file, \
            open(path, 'w') as new_file:
        new_file.write(current_file.read())
    os.remove(command_format[0])
