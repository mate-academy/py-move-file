import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv":
        mv, file_name, new_file_name = parts
        if "/" in new_file_name:
            way, name_file = os.path.split(new_file_name)
            os.makedirs(way, exist_ok=True)
            with (open(file_name, "r") as source,
                  open(new_file_name, "w") as new_file):
                new_file.write(source.read())
            os.remove(file_name)
        else:
            os.rename(file_name, new_file_name)
