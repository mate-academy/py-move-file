import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")
    if (len(command_parts) != 3
            or command_parts[0] != "mv"
            or not os.path.isfile(command_parts[1])):
        return

    _, source_path, dest_path = command_parts

    with open(source_path , "r") as source_file:
        content = source_file.read()

    new_file_path = dest_path.split("/")

    dir_path = ""
    for idx in range(len(new_file_path)):
        if new_file_path[idx].endswith(".txt"):
            dir_path = os.path.join(dir_path, new_file_path[idx])
            break
        dir_path = os.path.join(dir_path, new_file_path[idx])
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    with open(dir_path, "w") as dest_file:
        dest_file.write(content)
    os.remove(source_path)
