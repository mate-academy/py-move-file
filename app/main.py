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
    if file_name == old_file_path:
        raise ValueError("The source and destination represent "
                         "the same file.")
    if len(directory) == 0:
        with open(old_file_path, "r") as old_file:
            with open(new_file_path, "w") as new_file:
                new_file.write(old_file.read())
        os.remove(old_file_path)
    else:
        new_file_path = os.path.join(directory, file_name)
        new_directory = os.path.dirname(new_file_path)
        if not os.path.exists(new_directory):
            os.makedirs(new_directory, exist_ok=True)
        try:
            shutil.copy(old_file_path, new_file_path)
            os.remove(old_file_path)
        except OSError:
            raise OSError
