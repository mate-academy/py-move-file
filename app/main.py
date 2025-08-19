import os


def move_file(command: str) -> None:
    command_split = command.split()

    if len(command_split) != 3 and command_split[0] != "mv":
        print("Error: Invalid command format. "
              "Use 'mv source_path destination_path'")

        return

    source_path = command_split[1]
    destination_path = command_split[2]

    if destination_path[-1].endswith("/"):
        source_filename = os.path.basename(source_path)
        final_destination_path = os.path.join(destination_path,
                                              source_filename)
    else:
        final_destination_path = destination_path

    destination_dir = os.path.dirname(final_destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    try:
        with open(source_path, "r") as source_file:
            content = source_file.read()
    except FileNotFoundError:
        print(f"Error: Source file not found at {source_path}")
        return

    with open(final_destination_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_path)
