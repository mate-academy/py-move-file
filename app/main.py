import os


def move_file(command):

    command = command.split()
    file_curr = command.split()[1]
    file_curr_move = command.split("/")[-1]

    if command[0] != "mv":
        raise Exception("Command entered incorrectly!")

    with open(file_curr, "r") as curr_file:

        path = ""

        for directory in command.split()[2].split("/")[:-1]:
            path += directory + "/"
            os.mkdir(path)

        with open(path + file_curr_move, "w") as file_move:
            file_move.write(curr_file.read())

        os.remove(file_curr)
