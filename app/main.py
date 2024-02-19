import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "mv":
        source_file = parts[1]
        destination = parts[2]

        if not os.path.exists(source_file):
            raise FileNotFoundError\
                (f"The file '{source_file}' does not exist.")

        destination_directory = os.path.dirname(destination)
        if destination_directory:
            os.makedirs(destination_directory, exist_ok=True)

        os.replace(source_file, destination)
