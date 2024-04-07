import os


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) == 3 and command_list[0] == "mv":
        *_, in_file, out_file = command_list

        current_location = os.path.dirname(in_file)
        destination = os.path.dirname(out_file)

        if current_location == destination:
            os.rename(in_file, out_file)
        else:
            if destination:
                os.makedirs(destination, exist_ok=True)

            with (open(in_file, "r") as in_file,
                  open(out_file, "w") as out_file):
                out_file.write(in_file.read())
            os.remove(in_file.name)
