import os
import shutil


class SameNameError(Exception):
    pass


class CommandLineError(Exception):
    pass


def move_file(command: str) -> None:
    command_list = command.split()
    if command_list[0] == "mv" and len(command_list) == 3:
        _, first_file, second_file = command_list
    else:
        raise CommandLineError(f"Wrong command line please "
                               f"double check it: {command}")

    destination_path = os.path.dirname(second_file)
    new_file_name = os.path.basename(second_file)
    if destination_path:
        try:
            os.makedirs(destination_path, exist_ok=True)
        except OSError as e:
            raise OSError(f"{e}. Path is invalid, check "
                          f"for unaccepted symbols: '{destination_path}'")

    new_folder_path_plus_file = os.path.join(destination_path, new_file_name)
    if first_file == new_folder_path_plus_file:
        raise SameNameError("Same file, same name, "
                            "same folder, don't need to move")

    try:
        shutil.copy(first_file, new_folder_path_plus_file)
        os.remove(first_file)
        print("file moved successfully")
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    except OSError as e:
        raise OSError(f"{e} new_file_name is invalid check for unaccepted "
                      f"symbols: '{new_file_name}'")
