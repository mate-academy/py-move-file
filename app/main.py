import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) == 3 and commands[0] == "mv":
        mv, source, path_destination = commands
        if not os.path.isfile(source):
            raise FileNotFoundError(f"File not found: {source}")
        if (path_destination.endswith(("/", os.sep))
                or os.path.isdir(path_destination)):

            final_dir = path_destination
            final_name = os.path.join(path_destination,
                                      os.path.basename(source))

        else:
            final_dir = os.path.dirname(path_destination)
            final_name = path_destination

        if final_dir:
            os.makedirs(final_dir, exist_ok=True)

        with (open(source, "rb") as original_file,
              open(final_name, "wb") as new_file):
            for line in original_file:
                new_file.write(line)
        os.remove(source)
