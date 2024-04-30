import os


def move_file(command: str) -> None:
    parts = command.split()

    source_file, destination_path = parts[1], parts[2]

    if os.path.exists(source_file):
        if destination_path.endswith("/"):
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            destination_file = os.path.join(destination_path,
                                            os.path.basename(source_file))

        else:
            if os.path.isdir(destination_path):
                destination_file = os.path.join(destination_path,
                                                os.path.basename(source_file))
            else:
                destination_file = destination_path

                os.replace(source_file, destination_file)
