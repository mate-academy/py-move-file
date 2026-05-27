import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) == 3:
        action, file_name, path_destination = command_parts
        if action == "mv":
            if path_destination.endswith("/"):
                target_dir = path_destination
            else:
                target_dir = os.path.dirname(path_destination)
                if not target_dir:
                    target_dir = "."
            if os.path.isfile(target_dir):
                raise FileExistsError
            if target_dir and target_dir != ".":
                os.makedirs(target_dir, exist_ok=True)
            if path_destination.endswith("/"):
                full_path = os.path.join(path_destination, file_name)
            else:
                destination_folder = os.path.dirname(path_destination)
                destination_file = os.path.basename(path_destination)
                if not destination_folder:
                    full_path = destination_file
                else:
                    full_path = os.path.join(destination_folder,
                                             destination_file)
            with (open(file_name, "r") as file_in,
                  open(full_path, "w") as file_out):
                for line in file_in:
                    file_out.write(line)
            os.remove(file_name)
