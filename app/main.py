import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        print("Error: Invalid command format.")
        return

    source_file, destination = parts[1], parts[2]

    if not os.path.exists(source_file):
        print(f"Error: {source_file} does not exist.")
        return

    if not os.path.isfile(source_file):
        print(f"Error: {source_file} is a directory, not a file.")
        return

    if destination.endswith('/'):
        destination_dir = destination
        print(f"Creating directories: {destination_dir}")
        os.makedirs(destination_dir, exist_ok=True)
        destination = os.path.join(destination_dir, os.path.basename(source_file))

    else:
        if os.path.exists(destination):
            if os.path.isdir(destination):
                print(f"Error: A file with the name {os.path.basename(source_file)} already exists in the destination directory.")
            else:
                print(f"Error: {destination} already exists.")
            return

        destination_dir = os.path.dirname(destination)
        if destination_dir and not os.path.exists(destination_dir):
            print(f"Creating directories: {destination_dir}")
            os.makedirs(destination_dir, exist_ok=True)

    try:
        with open(source_file, "rb") as src:
            content = src.read()

        with open(destination, "wb") as dest:
            dest.write(content)
        print(f"Successfully moved {source_file} to {destination}.")

        os.remove(source_file)
        print(f"Removed the original file {source_file}.")

    except Exception as e:
        print(f"Error: {e}")
