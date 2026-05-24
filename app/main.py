import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    cmd, file_name, destination = command_parts
    if cmd != "mv":
        return
    path = destination.split("/")
    new_file = path[-1]
    path.pop(-1)
    current_path = ""
    for item in path:
        current_path = os.path.join(current_path, item)
        if not os.path.exists(current_path):
            os.mkdir(current_path)
    new_path = os.path.join(current_path, new_file)
    with open(file_name, "r") as file_in, open(new_path, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(file_name)
