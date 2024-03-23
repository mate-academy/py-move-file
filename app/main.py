import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "mv":
        if "/" not in command[2]:
            os.rename(command[1], command[2])
        else:
            directories = command[2].split("/")
            parent_directory = os.path.join(*directories[:-1])
            os.makedirs(parent_directory, exist_ok=True)
            with (
                open(command[1], "r") as src_file,
                open(command[2], "w") as dst_file
            ):
                data = src_file.read()
                dst_file.write(data)
            os.remove(command[1])
