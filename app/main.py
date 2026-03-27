from os import mkdir, remove, rename


def move_file(command: str):
    command = command.split(" ")
    if command[0] == "mv" and "/" in command[2]:
        lenght = 0
        for path in command[2].split("/")[:-1]:
            lenght += len(path) + 1
            mkdir(command[2][:lenght])

        with open(command[1], "r") as source, \
                open(command[2], "w") as target:
            text = source.read()
            target.write(text)
        remove(command[1])
    elif command[0] == "mv":
        rename(command[1], command[2])
