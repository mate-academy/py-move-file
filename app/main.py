from os import makedirs, remove, path

def move_file(command: str) -> None:
    parsed_cmd = command.split()
    if len(parsed_cmd) == 3 and parsed_cmd[0] == "mv":
        origin_file = parsed_cmd[1]
        dest_path = parsed_cmd[2]
        dest_dir = path.dirname(dest_path)
        new_file = path.basename(dest_path)
        if dest_path.endswith("/") or not new_file:
            new_file = path.basename(origin_file)
        if not dest_dir:
            dest_dir = "."
        if not path.exists(dest_dir):
            makedirs(dest_dir)
        with open(origin_file, "r") as origin, open(path.join(dest_dir, new_file), "w") as dest_file:
            data = origin.read()
            dest_file.write(data)

        remove(origin_file)