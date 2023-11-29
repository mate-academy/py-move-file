import os


def move_file(command: str) -> None:
    command_elements = command.split()
    if len(command_elements) == 3:
        command, file_name, new_path = command_elements
        if command == "mv":
            if new_path.endswith("/"):
                destination_directory = new_path
                destination_file_path = (
                    os.path.join(destination_directory, file_name)
                )
                try:
                    if not os.path.exists(destination_directory):
                        os.makedirs(destination_directory)
                    os.rename(file_name, destination_file_path)
                except FileNotFoundError:
                    raise FileNotFoundError(f"File '{file_name}' not found.")
            else:
                try:
                    new_path_dirs = new_path.split("/")
                    for i in range(1, len(new_path_dirs)):
                        directory_to_check = "/".join(new_path_dirs[:i])
                        if not os.path.exists(directory_to_check):
                            os.makedirs(directory_to_check)
                    os.rename(file_name, new_path)
                except FileNotFoundError:
                    raise FileNotFoundError(f"File '{file_name}' not found.")
