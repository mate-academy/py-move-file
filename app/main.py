import os
import re


def move_file(command: str) -> None:
    try:
        command, source_path, destination_path = command.split()
    except ValueError:
        print("Wrong command format")
    else:
        if command == "mv" and source_path != destination_path:
            if not os.path.isfile(source_path):
                raise ValueError(f"File '{source_path}' doesn't exist")
            source_path = os.path.join(*re.split(r"[\\/]", source_path))
            destination_path = os.path.join(
                *re.split(r"[\\/]", destination_path)
            )
            if (
                    source_path.endswith(os.sep)
                    or destination_path.endswith(os.sep)
            ):
                return

            if os.sep in destination_path:
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)

            with (
                open(source_path) as source,
                open(destination_path, "w") as destination
            ):
                destination.write(source.read())

            os.remove(source_path)
