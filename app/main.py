import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        mv_command, source_file, full_path = command_list
        if source_file != full_path and mv_command == "mv":

            if "/" in full_path:
                path, destination_file = os.path.split(full_path)

                if not os.path.exists(path):
                    os.makedirs(path)

                full_path = os.path.join(path, destination_file)

            with (open(source_file, "r") as source,
                  open(full_path, "w") as destination):
                destination.write(source.read())

            os.remove(source_file)
