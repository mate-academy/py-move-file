import os


def move_file(command: str) -> str:

    try:
        verb, source_file, path_to_outfile = command.split()
    except ValueError as e:
        return str(e)
    if verb != "mv":
        return "Not a valid command"

    destination_dir = os.path.dirname(path_to_outfile).split("/")
    destination_file = os.path.basename(path_to_outfile)

    if not destination_file:
        destination_file = source_file

    destination_path = ""
    if len(destination_dir) != 0:
        for subdirectory in destination_dir:
            if subdirectory != "":
                destination_path = os.path.join(destination_path, subdirectory)
                try:
                    os.mkdir(destination_path)
                except FileExistsError:
                    pass

    destination_path = os.path.join(destination_path, destination_file)
    try:
        with (open(source_file, "r") as file_in,
              open(destination_path, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError as e:
        return str(e)
    except PermissionError as e:
        return str(e)

    os.remove(source_file)
    return (f"File {source_file} has been moved to "
            f"{destination_path}")
