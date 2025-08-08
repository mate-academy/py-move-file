import os


def move_file(command: str) -> None:
    command_line = command.split()
    if len(command_line) != 3 or command_line[0] != "mv":
        return
    source_file = command_line[1]
    command_line = command_line[2].split("/")
    destination_file = command_line.pop(-1)
    destination_path = ""
    for command in command_line:
        try:
            destination_path += command
            os.mkdir(destination_path)
        except FileExistsError:
            continue
        finally:
            destination_path += "/"
    destination_path += destination_file
    try:
        with open(source_file, "r") as source, open(
            destination_path, "w"
        ) as destination:
            destination.write(source.read())
        os.remove(source_file)
    except FileNotFoundError:
        return
