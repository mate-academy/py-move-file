import os


def move_file(command: str) -> str | None:
    utilit, source_file_name, destination_file_name = command.strip().split()

    if utilit != "mv":
        return "Command must start with 'mv'"

    if not os.path.isfile(source_file_name):
        return f"{source_file_name} does not exist"

    if "/" not in destination_file_name:
        if source_file_name == destination_file_name:
            return "Destination_file_name already exists in this directory"
        os.rename(source_file_name, destination_file_name)
        return "File renamed successfully"

    if destination_file_name.endswith("/"):
        destination_file_name = os.path.join(
            destination_file_name,
            os.path.basename(source_file_name)
        )

    destination_path = os.path.dirname(destination_file_name)
    os.makedirs(destination_path, exist_ok=True)

    try:
        os.replace(source_file_name, destination_file_name)
    except (OSError, IOError) as e:
        return f"Error occurred while moving file: {e}"
