import os


def move_file(command: str) -> None:
    operation, source_file, new_file = command.split()
    if operation == "mv":
        path = os.path.dirname(new_file)
        if path:
            os.makedirs(path, exist_ok=True)

        with (
            open(source_file, "r") as source,
            open(new_file, "w") as new
        ):
            new.writelines(source.read())

        os.remove(source_file)
