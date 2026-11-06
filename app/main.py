import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    _, source_path, destination_path = command_parts

    if destination_path.endswith("/"):
        file_name = os.path.basename(source_path)
        folders = destination_path.rstrip("/").split("/")
    else:
        *folders, file_name = destination_path.split("/")

    current_path = ""
    for folder in folders:
        current_path = os.path.join(current_path, folder)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    destination_file_path = (
        os.path.join(current_path, file_name) if current_path else file_name
    )

    with open(source_path, "r") as source_file, \
            open(destination_file_path, "w") as target_file:
        target_file.write(source_file.read())

    os.remove(source_path)
