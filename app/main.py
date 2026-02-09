import os


def move_file(command: str) -> None:

    parts = command.split(" ")

    if len(parts) != 3:
        return

    mv, source, output = parts

    if mv != "mv":
        return

    if not os.path.exists(source) or not os.path.isfile(source):
        return

    if output.endswith("/"):
        output = os.path.join(output, os.path.basename(source))

    dir_to_create = os.path.dirname(output)
    if dir_to_create:
        dir_to_create = os.path.normpath(dir_to_create)
        current_path = ""
        for part in dir_to_create.split(os.sep):
            if current_path:
                current_path = os.path.join(current_path, part)
            else:
                current_path = part
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source, "r", encoding="utf-8") as src, \
         open(output, "w", encoding="utf-8") as otp:
        otp.write(src.read())

    os.remove(source)
