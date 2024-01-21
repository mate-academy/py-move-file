import os


def move_file(command: str) -> None:
    try:
        command, file_name, path = command.split()
        if file_name == path:
            return
        if command == "mv":
            directory, _ = os.path.split(path)
            if len(directory) != 0:
                os.makedirs(directory, exist_ok=True)
            with (open(file_name, "r") as file_in,
                  open(path, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_name)
    except ValueError:
        print("Something gone wrong, check input data")
