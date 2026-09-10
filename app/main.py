import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    command_name, source, destination = parts
    if command_name != "mv" or not os.path.isfile(source):
        return

    directory_path = (destination if destination.endswith("/")
                      else os.path.dirname(destination))
    if directory_path:
        current_path = ""
        for directory_name in directory_path.split(os.sep):
            current_path = os.path.join(current_path, directory_name)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    with (open(source, "r") as source_file,
          open(destination, "w") as destination_file):
        destination_file.write(source_file.read())
    os.remove(source)
