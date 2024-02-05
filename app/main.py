import os
import shutil


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        raise ValueError(f"Command must have 3 elements, but got: "
                         f"{len(command_list)}")
    move_command, old_file_path, new_file_path = command_list
    if move_command != "mv":
        raise NameError(f"{move_command} is not a valid")
    try:
        directory, file_name = os.path.split(new_file_path)
    except TypeError:
        raise TypeError(f"{new_file_path} is not string")
    if len(directory) == 0:
        try:
            shutil.copy(old_file_path, file_name)
            os.remove(old_file_path)
        except shutil.SameFileError:
            raise shutil.SameFileError("The source and destination represent "
                                       "the same file.")
    else:
        new_file_path = os.path.join(directory, file_name)
        new_directory = os.path.dirname(new_file_path)
        if not os.path.exists(new_directory):
            try:
                os.makedirs(new_directory)
            except FileExistsError:
                raise FileExistsError(f"The file cannot be created because "
                                      f"it already exists: {new_directory}")
        try:
            shutil.copy(old_file_path, new_file_path)
            os.remove(old_file_path)
        except OSError:
            raise OSError
