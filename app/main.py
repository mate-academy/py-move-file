import os


def move_file(command: str) -> None:
    command_components = command.split()
    if len(command_components) != 3:
        raise ValueError("Invalid command. "
                         "The command should be in the format: "
                         "mv <source> <destination>")
    if command_components[0] != "mv":
        raise ValueError("Invalid command. Only 'mv' is allowed.")
    source_name = command_components[1]
    destination_name = command_components[2]
    if not os.path.exists(source_name):
        raise FileNotFoundError(f"Source file '{source_name}' not found.")
    destination_folders = destination_name.split("/")[:-1]
    new_file_name = destination_name.split("/")[-1]
    new_path_to_create = ""
    for dir_name in destination_folders:
        new_path_to_create = os.path.join(new_path_to_create, dir_name)
        if not os.path.exists(new_path_to_create):
            os.mkdir(new_path_to_create)
    if not new_file_name:
        new_file_name = os.path.basename(source_name)
    new_path_to_create = os.path.join(new_path_to_create,
                                      new_file_name)
    with (open(source_name, "r") as source,
          open(new_path_to_create, "w") as moved
          ):
        moved.write(source.read())
    os.remove(source_name)
