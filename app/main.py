import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3:
        return
    if split_command[0] != "mv":
        return
    source = split_command[1]
    destination = split_command[2]
    if "/" in destination:
        parts = destination.split("/")
        current_path = ""
        for part in parts[:-1]:
            if current_path == "":
                current_path += part
            else:
                current_path += f"/{part}"
            if not os.path.exists(current_path):
                os.mkdir(current_path)
    if destination.endswith("/"):
        target_file = destination + source.split("/")[-1]
    else:
        target_file = destination
    with open(source, "r") as f_in, open(target_file, "w") as f_out:
        f_out.write(f_in.read())
    os.remove(source)
