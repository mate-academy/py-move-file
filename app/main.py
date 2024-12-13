from os import mkdir, remove


def move_file(command: str):
    command_new = command.split()
    if command_new[0] != "mv":
        return "Incorrect command!"
    if "/" in command_new[-1]:
        path = command_new[-1].split("/")
        for i in range(len(path) - 1):
            mkdir("/".join(path[:i]))
    with open(command_new[1], "r") as file_init, \
            open(command_new[2], "w") as file_out:
        file_out.write(file_init.read())
    return remove(command_new[1])
