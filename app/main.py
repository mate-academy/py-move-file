import os


def move_file(
        command: str) -> None:
    command_parts = command.split(" ")

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    command_name, source_path, destination_path = command_parts

    is_directory_only = destination_path.endswith(("/", "\\"))

    normalized_destination = destination_path.replace("\\", "/")
    destination_parts = normalized_destination.split("/")

    if is_directory_only:
        directory_parts = destination_parts[:-1]
        normalized_source = source_path.replace("\\", "/")
        source_parts = normalized_source.split("/")
        destination_file_name = source_parts[-1]
    else:
        directory_parts = destination_parts[:-1]
        destination_file_name = destination_parts[-1]

    current_directory = ""

    for part in directory_parts:
        if part == "":
            continue

        if current_directory == "":
            current_directory = part
        else:
            current_directory = os.path.join(current_directory, part)

        if not os.path.exists(current_directory):
            os.mkdir(current_directory)

    if current_directory == "":
        final_destination_path = destination_file_name
    else:
        final_destination_path = (os.path.join
                                  (current_directory, destination_file_name))

    with open(source_path, "r") as source_file_object:
        file_content = source_file_object.read()

    with open(final_destination_path, "w") as destination_file_object:
        destination_file_object.write(file_content)

    os.remove(source_path)
