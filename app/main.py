import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        return
    src = command_list[1]
    dst = command_list[2]
    if src == dst:
        return
    if os.path.isfile(src) and "/" not in dst:
        os.rename(src, dst)
    if "/" in dst:
        if not os.path.exists(src):
            return
        destination = dst.split("/")
        destination_file = destination.pop(-1)
        current_path = ""

        for part in destination:
            current_path = os.path.join(current_path, part)
            if not os.path.isdir(current_path):
                os.makedirs(current_path, exist_ok=True)
        full_path = os.path.join(current_path, destination_file)
        with (open(full_path, "w") as f, open(src, "r") as file):
            f.write(file.read())

        os.remove(src)
