import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv":
        source_file, destination_path = parts[1], parts[2]

        if os.path.exists(source_file):

            if destination_path.endswith("/"):
                destination_file = os.path.join(
                    destination_path,
                    os.path.basename(source_file))

            else:
                destination_file = destination_path

            destination_directory = os.path.dirname(destination_file)
            if destination_directory:
                os.makedirs(destination_directory, exist_ok=True)

            os.replace(source_file, destination_file)

            if os.path.exists(source_file):
                os.remove(source_file)
