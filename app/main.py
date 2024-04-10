import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3 and command_split[0] == "mv":
        comm, file_name, path = command_split

    if "/" not in path:
        with open(path, "w") as file:
            file.write("This is some\n content for\n the file.")
        return

    if path.endswith("/"):
        os.makedirs(path, exist_ok=True)
        with open(f"{path}/new_{file_name}", "w") as file:
            file.write("This is some\n content for\n the file.")
        return

    if path.endswith(".txt"):
        new_file_name = path.split("/")[-1]
        path_without_fn = "/".join(path.split("/")[:-1])
        os.makedirs(path_without_fn, exist_ok=True)
        with open(f"{path_without_fn}/{new_file_name}", "w") as file:
            file.write("This is some\n content for\n the file.")
