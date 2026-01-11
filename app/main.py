import os


def move_file(command: str) -> None:
    try:
        terminal_command, file_from, path_to = command.split(" ")
        check_command_mv(terminal_command)

        split_path_to = os.path.split(path_to)
        file_to = split_path_to[-1]
        directory_to = os.path.join(path_to[:path_to.index(file_to)])

        create_new_directory(directory_to)

        with open(file_from, "r") as out_file, open(path_to, "w") as in_file:
            in_file.write(out_file.read())

        os.remove(file_from)

    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)


def check_command_mv(terminal_command: str) -> None:
    if terminal_command != "mv":
        raise ValueError(f"command '{terminal_command}' is not 'mv'")


def create_new_directory(directory: str) -> None:
    if len(directory) > 0:
        os.makedirs(os.path.dirname(directory), exist_ok=True)
