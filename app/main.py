import os


def move_file(command: str) -> None:
    if not command:
        return

    command_units = command.split()

    if len(command_units) == 3 and command_units[0] == "mv":
        source_file = command_units[1]
        target_file = command_units[2]

        target_dir = os.path.dirname(target_file)

        if target_dir:
            os.makedirs(target_dir, exist_ok=True)

        if source_file != target_file:
            with (open(source_file, "r") as file_in,
                  open(target_file, "w") as file_out):
                for line in file_in:
                    file_out.write(line)

            os.remove(source_file)
