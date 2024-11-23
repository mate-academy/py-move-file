import os
import re


def move_file(command: str) -> None:
    cmd = command.strip().split()
    if cmd[0] != "mv" or len(cmd) != 3:
        raise (
            "Command must have 'mv' and exactly "
            "2 arguments (source and destination)"
        )
    current_path = "."
    file_source = command.split(" ")[1]
    file_destination = command.split(" ")[2]
    with open(
        file_source,
        "w",
    ) as f:
        f.write("This is some\n content for\n the file.")
    if "/" in command:
        folders = [
            folder[:-1]
            for folder in re.findall(r"(\w+/)", command.split(" ")[2])
        ]
        file_dest = command.split("/")[-1]
        for folder in folders:
            current_path = os.path.join(current_path, folder)
            os.makedirs(current_path, exist_ok=True)
        file_path = os.path.join(current_path, file_dest)
        with open(file_source, "r") as fl1, open(file_path, "w") as fl2:
            fl2.write(fl1.read())
        os.remove(file_source)
    else:
        with (
            open(file_source, "r") as fl11,
            open(file_destination, "w") as fl22,
        ):
            fl22.write(fl11.read())
        os.remove(file_source)
