import shutil
import os


def move_file(command: str) -> None:
    command_part = command.split()

    if command_part[0] == "mv":
        directories = command_part[2].split("/")[:-1]
        previous_directory = ""

        for directory in directories:

            if previous_directory == "":
                if not os.path.exists(directory):
                    os.mkdir(directory)
            else:
                if not os.path.exists(previous_directory + directory):
                    os.mkdir(previous_directory + directory)
            previous_directory += f"{directory}/"

        shutil.move(command_part[1], command_part[2])
