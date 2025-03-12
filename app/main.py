import os


def create_file(path_creating_file: str,
                name_future_file: str) -> None:
    with (open(path_creating_file, "r") as file_read,
          open(name_future_file, "w") as file_write):
        file_write.write(file_read.read())
    if os.path.exists(os.path.abspath(f"{name_future_file}")):
        os.remove(path_creating_file)


def move_file(command: str) -> None | str:
    result = command.split(" ")
    if len(result) >= 3 and result[0] == "mv":
        directory = result[-1].split("/")
        name_future_file = directory[-1]
        path_creating_file = os.path.abspath(f"{result[1]}")
        if len(directory) > 1:
            path_for_mkdir = os.path.join(
                "/".join(directory[:len(directory) - 1]))
            if not os.path.isdir(path_for_mkdir):
                try:
                    os.makedirs(path_for_mkdir)
                except FileNotFoundError:
                    pass
            named_directory = os.path.join(path_for_mkdir, name_future_file)
            try:
                create_file(path_creating_file, named_directory)
            except FileNotFoundError as error:
                return f"{error}"
        else:
            try:
                create_file(path_creating_file, name_future_file)
            except FileNotFoundError as error:
                return f"{error}"
    else:
        return "check your command"
