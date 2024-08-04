import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise SystemError("Command 'mv' must accept 3 arguments")

    _, source_path, destination_path = command.split()
    if destination_path.find("/") == -1 and destination_path.endswith(".txt"):
        os.rename(source_path, destination_path)

    else:
        if destination_path.split("/")[-1].endswith(".txt"):
            destination_dir_path = os.path.dirname(destination_path)
        else:
            destination_dir_path = destination_path

        if not os.path.exists(destination_dir_path):
            os.makedirs(destination_dir_path)

        with (
            open(source_path) as source_file,
            open(destination_path, "w") as destination_file
        ):
            for line in source_file:
                destination_file.write(line)

        os.remove(source_path)
