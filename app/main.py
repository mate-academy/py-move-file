import os


def move_file(command: str) -> None:
    cmd, source_file, destination_path, *_ = command.split()
    if cmd != "mv":
        return

    if os.path.exists(source_file):
        if os.path.isdir(destination_path):
            os.makedirs(destination_path, exist_ok=True)
            destination_file = os.path.join(destination_path,
                                            os.path.basename(source_file))

        else:
            if os.path.isdir(destination_path):
                destination_file = os.path.join(destination_path,
                                                os.path.basename(source_file))
            else:
                destination_dir = os.path.dirname(destination_path)
                if destination_dir and not os.path.exists(destination_dir):
                    os.makedirs(destination_dir, exist_ok=True)

                destination_file = destination_path
                os.replace(source_file, destination_file)
