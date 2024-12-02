import os


def move_file(command: str) -> None:
    split_command = command.split(" ")
    action, source, destination = split_command

    if len(split_command) != 3 or action != "mv":
        raise ValueError("Wrong command was entered!")

    if not os.path.isfile(source):
        raise FileNotFoundError("Please check existing of source file!")

    if destination.endswith("/") or "." not in os.path.basename(destination):
        if not os.path.exists(destination):
            os.makedirs(destination)
    else:
        folder_path = os.path.dirname(destination)
        if folder_path and not os.path.exists(folder_path):
            os.makedirs(folder_path)

    with (open(f"{source}", "r") as file_in,
          open(f"{destination}", "w+") as file_out):
        file_out.write(file_in.read())

    os.remove(source)
