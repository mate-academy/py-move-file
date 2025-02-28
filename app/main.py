import os


def move_file(command: str) -> None:
    split_command = command.split(" ")
    if (len(split_command) < 3
            or split_command[0] != "mv"
            or split_command[1] == split_command[2]):
        return

    path = split_command[2].split("/")
    path = "/".join(path[:-1])
    path = os.path.join("", path)

    try:
        os.makedirs(path)
    except FileExistsError:
        print(f"Dir {path} already exists")
    except FileNotFoundError:
        print("Rename file")

    try:
        with (open(split_command[1], "r") as file_in,
              open(split_command[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(split_command[1])
    except FileNotFoundError:
        print(f"Error: The file '{split_command[1]}' does not exist.")
