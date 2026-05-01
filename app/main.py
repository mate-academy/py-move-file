import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Invalid command format.")

    _, source_path, destination_path = command_parts

    if destination_path.endswith("/"):
        source_path_parts = source_path.split("/")
        source_file_name = source_path_parts[-1]
        destination_path = os.path.join(destination_path, source_file_name)

    destination_path_parts = destination_path.split("/")
    directory_parts = destination_path_parts[:-1]

    current_directory_path = ""

    for directory_name in directory_parts:
        if not directory_name:
            continue

        if current_directory_path == "":
            current_directory_path = directory_name
        else:
            current_directory_path = os.path.join(
                current_directory_path,
                directory_name
            )

        if not os.path.exists(current_directory_path):
            os.mkdir(current_directory_path)

    with open(source_path, "rb") as source_file_object:
        source_file_data = source_file_object.read()

    with open(destination_path, "wb") as destination_file_object:
        destination_file_object.write(source_file_data)

    os.remove(source_path)
