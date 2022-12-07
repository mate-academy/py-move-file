import os


def move_file(command):
    file_name = command.split()[1]
    file_move = command.split()[2]
    try:
        os.makedirs("/".join(file_move.split("/")[:-1]))
    except FileExistsError:
        pass
    try:
        os.rename(file_name, file_move)
    except FileNotFoundError:
        print("File is not exist, enter correct command, and try again")
