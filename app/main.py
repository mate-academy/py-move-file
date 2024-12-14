import os


def move_file(command: str) -> None:
    command_components = command.split()
    source_name = command_components[1]
    destination_name = command_components[2]
    is_valid_command = command_components[0] == "mv"
    is_valid_count_of_components = len(command_components) == 3

    if is_valid_command and is_valid_count_of_components:
        destination_folders = destination_name.split("/")[:-1]
        new_file_name = destination_name.split("/")[-1]
        new_path_to_create = ""

        for dir_name in destination_folders:
            new_path_to_create = os.path.join(new_path_to_create, dir_name)
            if not os.path.exists(new_path_to_create):
                os.mkdir(new_path_to_create)
        if new_file_name:
            new_path_to_create = os.path.join(new_path_to_create,
                                              new_file_name)
        else:
            current = source_name.split("/")[-1] \
                if "/" in source_name \
                else source_name
            new_path_to_create = os.path.join(new_path_to_create, current)

        with (open(source_name, "r") as source,
              open(new_path_to_create, "w") as moved
              ):
            moved.write(source.read())

        os.remove(source_name)
