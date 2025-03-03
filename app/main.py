import os


def move_file(command: str) -> None:
    split_command = command.split(" ")
    if (len(split_command) < 3
            or split_command[0] != "mv"
            or split_command[1] == split_command[2]):
        return

    source = split_command[1]
    destination = split_command[2]

    if not os.path.exists(source):
        print(f"Error: The file '{source}' does not exist.")
        return

    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))

    dest_dir = os.path.dirname(destination)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())

        os.remove(source)
        print(f"File moved from '{source}' to '{destination}'")

    except OSError as e:
        print(f"Error: {e}")

    try:
        with (open(split_command[1], "r") as file_in,
              open(split_command[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(split_command[1])
    except FileNotFoundError:
        print(f"Error: The file '{split_command[1]}' does not exist.")
