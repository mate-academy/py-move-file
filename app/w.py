import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3 or command_split[0] != "mv":
        return
    command_name, source_file, destination = command_split
    destination_file = (
        os.path.basename(destination)) if (
            os.path.basename(destination) != "") \
        else source_file
    destination_path = os.path.dirname(destination)
    if destination_path != "":
        if not os.path.exists(destination_path):
            print(destination_path)
            try:
                os.mkdir(destination_path)
            except FileNotFoundError:
                os.makedirs(destination_path)
    try:
        with (open(
                source_file,
                "r",
                newline="",
                encoding="utf-8") as read_file,
              open(
                  destination_file,
                  "w",
                  newline="",
                  encoding="utf-8") as write_file):
            for line in read_file:
                write_file.write(line)
        os.remove(source_file)
    except FileNotFoundError:
        return
