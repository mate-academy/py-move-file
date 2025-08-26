import os


def move_file(command: str) -> None:
    cmd, source_path, destination_path = command.split()
    if cmd != "mv":
        raise ValueError("Only 'mv' supported")

    if destination_path.endswith("/"):
        base_name = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, base_name)

    dir_path = os.path.dirname(destination_path)
    if dir_path and not os.path.isdir(dir_path):

        parts = dir_path.split("/")
        current_path = "."

        for part in parts:

            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with (open(source_path, "r") as file_in,
          open(destination_path, "w") as file_out):
        file_out.write(file_in.read())
    os.remove(source_path)
