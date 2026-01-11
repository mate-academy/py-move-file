import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Invalid command")
        return

    cmd, old_filename, destination = parts

    dir_path = os.path.dirname(destination)

    if cmd == "mv":
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        try:
            with (open(old_filename, "r") as file_in,
                  open(destination, "w") as file_out):
                file_out.write(file_in.read())

            os.remove(old_filename)
        except FileNotFoundError:
            print("File not found")
    else:
        print("Invalid command")
