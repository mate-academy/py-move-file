import os


def move_file(command: str) -> None:
    command, file, direct = command.split(" ")
    if command == "mv":
        new_direct = direct.split("/")
        if len(new_direct) > 1:
            os.makedirs("/".join(new_direct[:-1]), exist_ok=True)
    with open(file, "r") as original, open(direct, "w") as moved_file:
        moved_file.write(original.read())
    os.remove(file)
