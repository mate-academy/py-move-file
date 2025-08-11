import os


def move_file(command: str) -> None:
    command_list = command.split()
    command_name, source_path, destination_path = command_list
    if len(command_list) != 3 or command_name != "mv":
        return
    if not os.path.isfile(source_path):
        return
    destination_dir = os.path.dirname(destination_path)
    if not destination_dir:
        try:
            with (open(source_path, "r") as source_file,
                  open(destination_path, "w") as destination_file):
                destination_file.write(source_file.read())
            os.remove(source_path)
        except FileNotFoundError:
            pass
    elif destination_dir:
        try:
            if destination_path.endswith("/"):
                destination_dir = destination_path
                filename = os.path.basename(source_path)
                destination_path = os.path.join(destination_dir, filename)
            else:
                destination_dir = os.path.dirname(destination_path)
            parts = destination_dir.split("/")
            current_path = ""
            for part in parts:
                current_path = os.path.join(current_path, part)
                if not os.path.exists(current_path):
                    os.mkdir(current_path)
            with (open(source_path, "r") as source_file,
                  open(destination_path, "w") as destination_file):
                destination_file.write(source_file.read())
            os.remove(source_path)
        except (FileNotFoundError, FileExistsError, PermissionError):
            pass
