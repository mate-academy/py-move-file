from os import mkdir, remove, rename, path


def move_file(command: str) -> None:
    command_list: list = command.split()
    if (
            len(command_list) == 3
            and command_list[0] == "mv"
            and path.isfile(command_list[1])
    ):
        if "/" not in command_list[2]:
            rename(command_list[1], command_list[2])
        else:
            path_list: list = command_list[2].split("/")
            full_path: str = ""
            for directory in path_list[:-1]:
                full_path = path.join(full_path, directory)
                if not path.exists(full_path):
                    mkdir(full_path)
            with (
                open(command_list[1], "r") as source_file,
                open(command_list[2], "w") as destination_file
            ):
                source: str = source_file.read()
                destination_file.write(source)
            remove(command_list[1])
