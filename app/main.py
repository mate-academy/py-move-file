import os


def move_file(command: str) -> None:
    name_file = command.split(" ")
    if len(name_file) != 3:
        raise Exception("Input error")
    if name_file[0] == "mv":
        source_file = name_file[1]
        destination_file = name_file[2]
        destination_dir = os.path.dirname(destination_file)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(source_file)
