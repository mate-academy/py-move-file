import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        operation, filename, destination_to_new_file = command_parts
        if (
                operation == "mv"
                and os.path.exists(filename)
        ):
            with open(filename, "r") as f:
                file_content = f.read()

            os.remove(filename)

            folder = os.path.dirname(destination_to_new_file)

            if folder:
                os.makedirs(folder, exist_ok=True)

            with open(destination_to_new_file, "w") as f:
                f.write(file_content)
