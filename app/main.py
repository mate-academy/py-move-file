import os


def move_file(command: str) -> None:
    cleared_command: list[str] = command.split()
    if len(cleared_command) != 3 or cleared_command[0] != "mv":
        raise (ValueError
               ("Invalid command format. Use 'mv source destination'."))

    _, source, destination = cleared_command

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    if destination.endswith("/"):
        if (os.path.exists(destination)
                and not os.path.isdir(destination)):
            raise FileExistsError(f"'{destination}' "
                                  f"exists and is not a directory.")
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        destination_dir: str = os.path.dirname(destination)
        if destination_dir:
            if (os.path.exists(destination_dir)
                    and not os.path.isdir(destination_dir)):
                raise FileExistsError(f"'{destination_dir}' "
                                      f"exists and is not a directory.")
            os.makedirs(destination_dir, exist_ok=True)

    if os.path.exists(destination):
        raise FileExistsError(f"Destination '{destination}' already exists.")

    with open(source, "r") as src_file:
        content: str = src_file.read()

    with open(destination, "w") as dest_file:
        dest_file.write(content)

    os.remove(source)
