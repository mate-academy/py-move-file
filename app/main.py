import os


def move_file(command: str) -> None:
    new_line = command.split()
    if len(new_line) != 3 or new_line[0] != "mv":
        return

    _, source, destination_str = new_line
    parts = destination_str.split("/")
    list_dir = parts[:-1]
    current_path = ""
    for item in list_dir:
        current_path = os.path.join(current_path, item)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    if destination_str.endswith("/"):
        destination = os.path.join(destination_str, os.path.basename(source))
    else:
        destination = destination_str

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(source)
    except FileNotFoundError:
        return
