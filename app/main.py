import os


def move_file(command: str) -> None:
    operation, old_file, new_file = command.split()

    if operation == "mv" and old_file != new_file:
        new_path, _ = os.path.split(new_file)
        if new_path:
            os.makedirs(new_path, exist_ok=True)

        with open(old_file, "r") as reader, open(new_file, "w") as writer:
            writer.write(reader.read())
        os.remove(old_file)
