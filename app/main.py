import os


def move_file(command: str) -> None:
    *_, in_file, out_file = command.split(" ")
    current_location = os.path.dirname(in_file)
    destination = os.path.dirname(out_file)

    if current_location == destination:
        os.rename(in_file, out_file)
    else:
        if not os.path.exists(destination):
            os.makedirs(destination)

        with (open(in_file, "r") as in_file,
              open(out_file, "w") as out_file):
            out_file.write(in_file.read())
        os.remove(in_file.name)
