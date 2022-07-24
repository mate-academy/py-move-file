import os
import pathlib
import shutil


def move_file(command: str):
    command_list = command.split(" ")

    # define variables which contain the paths
    source = command_list[1]
    destination = command_list[2]

    # get a path without name of file
    path = destination.split("/")[0:-1]
    directory = "/".join(path)

    # create path if its not exist
    if not os.path.isdir(destination):
        pathlib.Path(directory).mkdir(parents=True, exist_ok=True)

    # move file to specified directory
    shutil.move(source, destination)
