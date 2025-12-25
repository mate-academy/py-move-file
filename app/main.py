import os


def move_file(command: str) -> None:
    command_parts = command.split()
    src = ""
    dst = ""

    if command_parts and command_parts[0] == "mv":
        src = command_parts[1]
        dst = command_parts[2]

    if "/" in dst:
        dir_path = os.path.dirname(dst)
        os.makedirs(dir_path, exist_ok=True)

        with open(src, "r") as original_file, open(dst, "w") as new_file:
            for line in original_file:
                new_file.write(line)

        os.remove(src)
    elif ("/" not in dst) and (src != dst):
        os.rename(src, dst)
