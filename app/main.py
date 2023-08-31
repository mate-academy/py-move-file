import os


def move_file(command: str) -> None:
    command_parts = command.split()

    try:
        command, source_path, new_path = command_parts
    except ValueError as e:
        print(f"Invalid command: {e}")
        return

    if command == "mv":
        path, destination_file = os.path.split(new_path)

        if path:
            os.makedirs(path, exist_ok=True)

        with (
            open(source_path, "r") as source,
            open(new_path, "w") as new_path
        ):
            new_path.write(source.read())

        os.remove(source_path)

    else:
        os.rename(source_path, new_path)
