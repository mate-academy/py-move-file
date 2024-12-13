from os import remove, makedirs, path


def move_file(command: str) -> None:
    if command.startswith("mv "):
        commands, first_file_name, second_file_name = command.split()
        if "/" in second_file_name:
            paths = path.split(second_file_name)[0]
            makedirs(paths, exist_ok=True)
        with (open(first_file_name, "r") as file_to_copy,
              open(second_file_name, "w") as file_copy):
            file_copy.write(file_to_copy.read())
        remove(first_file_name)
