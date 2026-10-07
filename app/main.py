import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3:
        raise ValueError("wrong command")
    cmd, source_file , destination_file = parts
    if not cmd == "mv":
        return

    with open(source_file , "r") as old_f:
        new_path = destination_file
        if destination_file.endswith("/"):
            new_path = os.path.join(
                destination_file,
                os.path.basename(source_file)
            )

        folder = os.path.dirname(new_path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(new_path, "w") as new_f:
            new_f.write(old_f.read())
        pass

    os.remove(source_file)
