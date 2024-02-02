import os


def move_file(command: str) -> None:
    linux_command, old_file, path_to_new_file = command.split()

    if (
            len(command.split()) == 3
            and linux_command == "mv"
            and not old_file == path_to_new_file
    ):
        if "/" not in path_to_new_file:
            os.rename(old_file, path_to_new_file)
        else:
            directories = os.path.dirname(path_to_new_file)

            os.makedirs(directories, exist_ok=True)

            os.replace(old_file, path_to_new_file)
