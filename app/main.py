import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    path_parts = destination.split("/")
    file_name = path_parts[-1]
    directory_parts = path_parts[:-1]

    current_path = ""
    for directory in directory_parts:
        current_path = (
            os.path.join(current_path, directory)
            if current_path
            else directory
        )
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    destination_path = (
        os.path.join(current_path, file_name) if current_path else file_name
    )

    with open(source, "r") as file_in, open(destination_path, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
