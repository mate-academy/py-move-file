import os


def move_file(command: str) -> None:
    parts = command.split()
    source_file = parts[1]
    destination = parts[2]
    path_parts = destination.split("/")

    if destination[-1] == "/":
        filename = source_file.split("/")[-1]
        dir_parts = path_parts[:-1] if path_parts[-1] == "" else path_parts
    else:
        filename = path_parts[-1]
        dir_parts = path_parts[:-1]

    current_path = ""
    for i in range(len(dir_parts)):
        if i == 0:
            current_path = dir_parts[i]
        else:
            current_path = current_path + "/" + dir_parts[i]

        try:
            os.mkdir(current_path)
        except (FileExistsError, OSError):
            pass

    if len(dir_parts) > 0:
        new_file_path = current_path + "/" + filename
    else:
        new_file_path = filename

    with open(source_file, "r") as original_file:
        file_content = original_file.read()

    with open(new_file_path, "w") as new_file:
        new_file.write(file_content)

    os.remove(source_file)
