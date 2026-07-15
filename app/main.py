import os


def move_file(command: str) -> None:
    tokens = command.split(" ")
    if len(tokens) != 3:
        return
    if tokens[0] != "mv":
        return
    _, source, destination = tokens[0], tokens[1], tokens[2]
    if "/" not in destination:
        os.rename(source, destination)
    elif "/" in destination:
        direc = destination.split("/")
        file_name, parts = direc[-1], direc[:-1]
        current_path = ""
        for part in parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        if not file_name:
            file_name = os.path.basename(source)
        with open(
            source,
            "r"
        )as origin, open(
            os.path.join(current_path, file_name),
            "w"
        ) as new_f:
            new_f.write(origin.read())
        os.remove(source)
