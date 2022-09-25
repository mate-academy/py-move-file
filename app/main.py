import os


def move_file(command: str) -> None:
    command = command.split()
    command[2] = command[2].split("/")
    command.append(command[2][-1])
    command[2] = "/".join(command[2][:-1])

    if command[2] != '':
        os.makedirs(command[2])
        command[2] += '/'
    with (open(command[1], "r") as old_file,
          open(f"{command[2]}{command[3]}", "w") as new_file):
        new_file.write(old_file.read())
    os.remove(command[1])
