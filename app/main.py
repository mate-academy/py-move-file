import os


def move_file(command: str) -> str | None:
    parts = command.strip().split()

    if len(parts) != 3:
        return "Invalid command format. Must be: mv <source> <destination>"

    utilit, source_file_name, destination_file_name = parts

    if utilit != "mv":
        return "Command must start with 'mv'"

    if not os.path.isfile(source_file_name):
        return f"{source_file_name} does not exist"

    if not os.path.dirname(destination_file_name):
        if source_file_name == destination_file_name:
            return "Destination file already exists in this directory"
        try:
            with (open(source_file_name, "r") as src,
                  open(destination_file_name, "w") as dst):
                dst.write(src.read())
            os.remove(source_file_name)
            return "File renamed successfully"
        except (OSError, IOError) as e:
            return f"Error occurred while moving file: {e}"

    if destination_file_name.endswith(os.sep):
        destination_file_name = os.path.join(
            destination_file_name,
            os.path.basename(source_file_name)
        )

    destination_path = os.path.dirname(destination_file_name)
    os.makedirs(destination_path, exist_ok=True)

    try:
        with (open(source_file_name, "r") as src,
              open(destination_file_name, "w") as dst):
            dst.write(src.read())
        os.remove(source_file_name)
        return "File moved successfully"
    except (OSError, IOError) as e:
        return f"Error occurred while moving file: {e}"
