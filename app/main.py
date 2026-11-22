import os


def move_file(command: str) -> None:
    new_command = command.split()
    if len(new_command) != 3 or new_command[0] != "mv":
        return None
    path_of_source_file = new_command[1]
    path_of_destiny = new_command[2]

    if path_of_destiny.endswith("/"):
        name_start = os.path.basename(path_of_source_file)
        way = os.path.join(path_of_destiny, name_start)
    else:
        way = path_of_destiny

    current_path = os.path.dirname(way)

    if current_path:
        list_of_directories = current_path.split("/")
    else:
        list_of_directories = []
    beginning = os.path.abspath(path_of_source_file)
    destination = os.path.abspath(way)

    if beginning == destination:
        return None

    if os.path.isabs(current_path):
        current_dir = "/"
    else:
        current_dir = ""

    if current_dir == "/":
        list_of_directories.pop(0)

    for directory in list_of_directories:
        current_dir = os.path.join(current_dir, directory)

        if not os.path.exists(current_dir):
            os.mkdir(current_dir)

    with open(path_of_source_file, "r") as file_in, open(way, "w") as file_out:
        content = file_in.read()
        file_out.write(content)

    os.remove(path_of_source_file)
