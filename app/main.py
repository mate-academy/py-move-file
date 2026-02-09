import os


def move_file(command: str) -> None:

    parts = command.split(" ")

    mv, source, output = parts

    dir_to_create = ""

    if mv != "mv" or len(parts) != 3:
        return

    if not os.path.exists(source):
        return

    if output.endswith("/"):
        output = os.path.join(output, os.path.basename(source))

    dir_to_create = os.path.dirname(output)
    if dir_to_create:
        os.makedirs(dir_to_create, exist_ok=True)

    with open(source, "r", encoding="utf-8") as src, \
         open(output, "w", encoding="utf-8") as otp:
        otp.write(src.read())

    os.remove(source)
