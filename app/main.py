import os


def move_file(command: str) -> None:
    if command.count(" ") != 2:
        return

    tokens = command.split(" ")
    if tokens[0] != "mv":
        return

    source_file_name = tokens[1]
    destination_file_name = tokens[2]

    if source_file_name == destination_file_name:
        return

    try:
        if destination_file_name.endswith("/"):
            os.makedirs(destination_file_name, exist_ok=True)
            destination_file_name = os.path.join(destination_file_name, os.path.basename(source_file_name))
        else:

            dest_dir = os.path.dirname(destination_file_name)
            if dest_dir:
                os.makedirs(dest_dir, exist_ok=True)

        with open(source_file_name, "r") as file_in, open(destination_file_name, "w") as file_out:
            file_out.write(file_in.read())

        os.remove(source_file_name)

    except FileNotFoundError:
        pass
