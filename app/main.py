import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command")
        return

    source_file = parts[1]
    destination_path = parts[2]

    if not os.path.isfile(source_file):
        print(f"Error: {source_file} does not exist.")
        return

    if not os.path.basename(destination_path):
        print("Error: Destination must include a file name,"
              " not just a directory path.")
        return

    destination_dir = os.path.dirname(destination_path)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    try:
        os.rename(source_file, destination_path)
        print(f"Moved {source_file} to {destination_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
