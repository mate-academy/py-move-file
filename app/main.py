import os


def move_file(command: str) -> None:
    split_command = command.split(" ")

    if len(split_command) < 3 or split_command[0] != "mv":
        print("Error: Invalid command format.")
        return

    source = split_command[1]
    destination = split_command[2]

    if source == destination:
        print("Error: Source and destination are the same.")
        return

    if not os.path.exists(source):
        print(f"Error: The file '{source}' does not exist.")
        return

    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))

    dest_dir = os.path.dirname(destination)
    if dest_dir and not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
        except OSError as e:
            print(f"Error creating directory '{dest_dir}': {e}")
            return

    try:
        os.replace(source, destination)
        print(f"File moved from '{source}' to '{destination}'")
    except OSError as e:
        print(f"Error moving file: {e}")
