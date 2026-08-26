import os


def move_file(command: str) -> None:

    command_parts = command.split(" ")
    if os.path.isdir(command_parts[2]):
        command_parts[2] = command_parts[2] + "/" + command_parts[1]
    if "/" in command_parts[2]:
        path, new_file = command_parts[2].rsplit("/", 1)
        parts = path.split("/")
        for i in range(len(parts)):
            current_path = "/".join(parts[:i + 1])
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        with open(command_parts[2], "w") as f:
            f.write(open(command_parts[1], "r").read())
    else:
        with open(command_parts[2], "w") as f:
            f.write(open(command_parts[1], "r").read())
    os.remove(command_parts[1])
