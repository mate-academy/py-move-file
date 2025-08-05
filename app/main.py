import os


def move_file(command: str) -> None:
    command_parts = command.strip().split(" ", 2)

    if len(command_parts) != 3:
        print("Error: The command format is incorrect")
        return

    command_name, source_path, destination_path = command_parts

    if command_name != "mv":
        print("Error: The command is not 'mv'")
        return

    if destination_path.endswith("/"):
        file_name = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, file_name)

    if "/" not in destination_path:
        os.rename(source_path, destination_path)
        return

    destination_directory = os.path.dirname(destination_path)

    if destination_directory and not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    with open(source_path, "rb") as source_file:
        file_content = source_file.read()

    with open(destination_path, "wb") as destination_file:
        destination_file.write(file_content)

    os.remove(source_path)
