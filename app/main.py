import os


def move_file(command: str) -> None:

    command_list = command.split(" ")

    if len(command_list) != 3 or command_list[0] != "mv":
        raise ValueError("Invalid command fomat.")

    _, file_to_copy, destination_path = command_list

    if destination_path.endswith("/"):
        source_filename = os.path.basename(file_to_copy)
        destination_path = os.path.join(destination_path, source_filename)

    destination_dir = os.path.dirname(destination_path)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    with open(file_to_copy, "r") as file:
        data = file.read()

    with open(destination_path, "w") as file:
        file.write(data)

    os.remove(file_to_copy)
