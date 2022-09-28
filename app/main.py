import os


def move_file(command: str) -> None:
    command = command.split()[1:]
    if "/" not in command[1]:
        os.rename(command[0], command[1])
    else:
        path = command[1].split('/')
        true_path = ""
        for i in range(len(path) - 1):
            true_path += path[i]
            os.mkdir(true_path)
            true_path += "/"
        with open(command[0], "r") as file_in, \
                open(command[1], "w") as file_out:
            for line in file_in.read()
                file_out.write(line)
    os.remove(command[0])
