import os


def move_file(command: str) -> None:
    new_line = command.split()
    if len(new_line) != 3 or new_line[0] != "mv":
        return

    parts = new_line[2].split("/")
    list_dir = parts[:-1]
    source = new_line[1]
    current_path = ""
    for item in list_dir:
        current_path += item + "/"
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    if new_line[2].endswith("/"):
        destination = new_line[2] + source
    else:
        destination = new_line[2]

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(source)
    except FileNotFoundError:
        return
