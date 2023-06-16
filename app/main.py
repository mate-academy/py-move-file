import os


def move_file(command):
    command = command.split()
    if "/" not in command[2]:
        os.rename(command[1], command[2])

    patch = "/".join(command[2].split('/')[0:-1])
    name = command[2].split('/')[-1]
    os.rename(command[1], name)
    os.makedirs(patch)

    os.replace(name, f"{patch}/{name}")
