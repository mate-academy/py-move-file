from os import remove, makedirs


def move_file(command: str) -> None:
    if command.startswith("mv "):
        commands = command.split()
        first_file_name = commands[1]
        second_file_name = commands[2]
        if "/" in second_file_name:
            paths = "".join([
                directory + "/"
                for directory in second_file_name.split("/")
                if "." not in directory
            ])
            try:
                makedirs(paths)
            except FileExistsError:
                pass
        with (open(first_file_name, "r") as file_to_copy,
              open(second_file_name, "w") as file_copy):
            file_copy.write(file_to_copy.read())
        remove(first_file_name)
