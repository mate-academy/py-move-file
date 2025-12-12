import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and split_command[0] == "mv":
        source_file, target_path = split_command[1:]
        if target_path.endswith(os.path.sep):
            directory_to_create = target_path
            final_destination = os.path.join(target_path,
                                             os.path.basename(source_file))
        elif os.path.dirname(target_path):
            directory_to_create = os.path.dirname(target_path)
            final_destination = target_path
        else:

            directory_to_create = ""
            final_destination = target_path

        if directory_to_create:

            os.makedirs(directory_to_create, exist_ok=True)

        try:
            with (open(source_file, "r") as file_in,
                  open(final_destination, "w") as file_out):
                file_out.write(file_in.read())

            os.remove(source_file)

        except FileNotFoundError:
            pass
