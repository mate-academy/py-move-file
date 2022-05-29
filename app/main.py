import os
import shutil


def move_file(command: str):
    command_ls = command.replace("/", "\\").split()
    name_of_command = command_ls[0]
    name_of_file = command_ls[1]
    name_and_way_new_file = command_ls[2]

    assert name_of_command == "mv", f"Command:{name_of_command} is not defined"

    if "/" not in command:
        original = rf'{os.getcwd()}\{name_of_file}'
        target = rf'{os.getcwd()}\{name_and_way_new_file}'
        shutil.copyfile(original, target)
        os.remove(name_of_file)
        print("Operation completed")
    else:
        # path to create new directories
        path_to_directory = list(name_and_way_new_file)
        path_to_directory.reverse()
        path_to_directory_copy = path_to_directory[:]
        for x in path_to_directory_copy:
            if x != "\\":
                path_to_directory.remove(x)
            else:
                path_to_directory.remove(x)
                break
        path_to_directory.reverse()
        path_to_directory = "".join(path_to_directory)
        path_to_create_directories = os.path.join(
            os.getcwd(), path_to_directory
        )

        # create directories
        os.makedirs(path_to_create_directories)

        # copy file
        original = rf'{os.getcwd()}\{name_of_file}'
        target = rf'{os.getcwd()}\{name_and_way_new_file}'
        shutil.copyfile(original, target)

        # remove old file
        os.remove(name_of_file)

        print("Operation completed")
