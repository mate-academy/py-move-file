import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        operation, filename, destination = command_parts
        if (
                operation == "mv"
                and os.path.exists(filename)
        ):
            with open(filename, "r") as f:
                file_content = f.read()

            os.remove(filename)

            raw_destination = destination

            destination = os.path.normpath(destination)

            if raw_destination.endswith(("\\", "/")):
                destination = os.path.join(
                    destination, os.path.basename(filename)
                )

            current_path = ""
            folders = os.path.dirname(destination).split(os.sep)
            for folder in folders:
                if folder:
                    current_path = os.path.join(current_path, folder)
                    try:
                        os.mkdir(current_path)
                    except FileExistsError:
                        ...

            with open(destination, "w") as f:
                f.write(file_content)
