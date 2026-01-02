import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) == 3 and commands[0] == "mv":
        mv, source, path_destination = commands
        if not os.path.isfile(source):
            raise FileNotFoundError(f"File not found: {source}")
        # if path_destination[-1] == "/" or path_destination[-1] == os.sep:
        if (path_destination.endswith(("/", os.sep))
                or os.path.isdir(path_destination)):
            os.makedirs(path_destination, exist_ok=True)
            with (open(source, "rb") as original_file,
                  open(os.path.join(path_destination,
                                    os.path.basename(source)),
                       "wb") as new_file):
                for line in original_file:
                    new_file.write(line)
            os.remove(source)

        else:
            final_path = os.path.dirname(path_destination)
            if final_path:
                os.makedirs(final_path, exist_ok=True)

            with (open(source, "rb") as original_file,
                  open(path_destination, "wb") as new_file):
                for line in original_file:
                    new_file.write(line)
            os.remove(source)
