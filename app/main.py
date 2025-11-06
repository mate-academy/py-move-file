from os import remove, rename, makedirs, path


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) == 3:
        command = command_list[0]
        file_to_copy = command_list[1]
        directory = ""
        new_file = command_list[2]
        if file_to_copy == new_file:
            return

        if "/" in command_list[2]:
            cleared_path = command_list[2].split("/")
            directory = "/".join(cleared_path[:-1])
            if not cleared_path[-1]:
                new_file = file_to_copy
            else:
                new_file = cleared_path[-1]

        full_path = path.join(directory, new_file)

        if command == "mv":
            if not directory:
                try:
                    rename(file_to_copy, new_file)
                    return
                except FileExistsError:
                    raise FileExistsError

            makedirs(directory, exist_ok=True)

            try:
                with open(file_to_copy, mode="r") as file_read:
                    file_data = file_read.readlines()

                with open(full_path, mode="w") as file_write:
                    file_write.write("".join(file_data))

                remove(file_to_copy)
            except FileNotFoundError:
                raise FileNotFoundError("[Errno 2] No such file or directory")
