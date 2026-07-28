import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    src = command_parts[1]
    dst = command_parts[2]

    if not os.path.exists(src):
        return

    # Если путь заканчивается на / или \ — это каталог
    if dst.endswith("/") or dst.endswith("\\"):
        dst = os.path.join(dst, os.path.basename(src))

    dst_dir = os.path.dirname(dst)

    if dst_dir:
        # Нормализуем путь (Windows/Linux)
        dst_dir = os.path.normpath(dst_dir)

        current = ""

        for part in dst_dir.split(os.sep):
            current = os.path.join(current, part) if current else part

            if not os.path.exists(current):
                os.mkdir(current)

    with open(src, "r") as old_file, open(dst, "w") as new_file:
        new_file.write(old_file.read())

    os.remove(src)
