import os


def move_file(command: str) -> None:
    command_parts = command.split()
    current_path = ""
    if len(command_parts) == 3 and command_parts[0] == "mv":
        source_name = command_parts[1]
        destination_name = command_parts[2]
        if destination_name.endswith("/"):
            source_file_name = os.path.basename(source_name)
            destination_name += source_file_name
        if source_name == destination_name:
            return
        destination_parts = destination_name.split("/")
        directory_parts = destination_parts[:-1]
        for directory in directory_parts:
            if current_path == "":
                current_path = directory
            else:
                current_path += "/" + directory
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        try:
            with open(source_name, "r") as source_file, open(
                    destination_name, "w"
            ) as destination_file:
                destination_file.write(source_file.read())
            os.remove(source_name)
        except FileNotFoundError:
            return
