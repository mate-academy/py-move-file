import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        raise ValueError(f"Invalid command: {command}, expected 3 arguments")
    if command_split[0] != "mv":
        raise ValueError("First argument must be 'mv'")
    cmd, source_file, new_file = command_split
    if new_file.endswith("/"):
        new_dir = new_file
        new_file = os.path.join(new_dir, os.path.basename(source_file))
    else:
        new_dir = os.path.dirname(new_file)
    os.makedirs(os.path.abspath(new_dir), exist_ok=True)
    try:
        with (open(source_file, "r") as file_in,
              open(os.path.join(
                  new_dir,
                  os.path.basename(new_file)
              ), "w") as file_out):
            file_out.write(file_in.read())
        os.remove(source_file)
    except OSError:
        raise
