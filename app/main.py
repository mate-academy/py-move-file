import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    comm, file_name, file_way = parts
    if file_way[-1] == "/":
        file_way = file_way + file_name
    if comm != "mv":
        return
    way_parts = file_way.split("/")
    dirs = way_parts[:-1]
    current_path = ""
    for folder in dirs:
        current_path = os.path.join(current_path, folder)
        if not os.path.exists(current_path):
            os.mkdir(current_path)
    with open(file_name) as file_1, open(file_way, "w") as file_2:
        file_2.write(file_1.read())
    os.remove(file_name)
