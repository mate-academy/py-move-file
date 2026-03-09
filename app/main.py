import os


def move_file(command: str) -> None:
    command_elements = command.split()

    if len(command_elements) != 3:
        return

    if command_elements[0] != "mv":
        return

    _, source_file_name, destination_file_name = command_elements

    try:
        with open(source_file_name, "r") as source_file:
            content = source_file.read()

        os.remove(source_file_name)

        folder_path, filename = os.path.split(destination_file_name)

        if folder_path:
            os.makedirs(folder_path, exist_ok=True)

        if not filename:
            destination_file_name = os.path.join(folder_path, source_file_name)

        with open(destination_file_name, "w") as destination_file:
            destination_file.write(content)

    except FileNotFoundError:
        pass
