import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        print("Invalid command format. Please provide a valid command.")
        return

    comand, source_file, destination = parts

    if comand == "mv" and source_file != destination:
        source_file = os.path.normpath(source_file)
        destination = os.path.normpath(destination)
        if destination.endswith("/"):
            destination_dir = destination
            file_name = os.path.basename(source_file)
            destination_path = os.path.join(destination_dir, file_name)
        else:
            destination_path = destination

        destination_directory = os.path.dirname(destination_path)
        if destination_directory:
            os.makedirs(destination_directory, exist_ok=True)

        os.rename(source_file, destination_path)
