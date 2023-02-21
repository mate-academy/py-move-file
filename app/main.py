import os


def move_file(command: str) -> None:
    operation, old_file_loc, new_file_loc = command.split()

    if operation == "mv" and old_file_loc != new_file_loc:
        new_path, _ = os.path.split(new_file_loc)
        if new_path:
            os.makedirs(new_path, exist_ok=True)

        with open(old_file_loc, "r") as reader:
            with open(new_file_loc, "w") as writer:
                writer.write(reader.read())
        os.remove(old_file_loc)
