from pathlib import Path
import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    command_type, source_file_name, destination_file_name = command_parts

    if command_type == "mv":
        if source_file_name == destination_file_name:
            return

        dir_sep = os.sep if os.sep in source_file_name else "/"

        is_destination_directory = (Path(destination_file_name).is_dir()
                                    or destination_file_name.endswith(dir_sep))

        if is_destination_directory:
            final_destination = os.path.join(
                destination_file_name,
                os.path.basename(source_file_name))
        else:
            final_destination = destination_file_name

        parent_dir = os.path.dirname(final_destination)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        with (open(source_file_name, "rb") as source_file_object,
              open(final_destination, "wb") as destination_file_object):
            destination_file_object.write(source_file_object.read())

        os.remove(source_file_name)
