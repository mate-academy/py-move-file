from os import makedirs, remove, path

# write your code here
def move_file(command: str) -> None:
    parsed_cmd = command.split()
    if len(parsed_cmd) == 3:
        cmd = parsed_cmd[0]
        origin_file = parsed_cmd[1]
        dest = path.dirname(parsed_cmd[2])
        new_file = path.basename(parsed_cmd[2])
        if cmd == "mv":
            if not dest:
                with (
                    open(origin_file, "r") as origin,
                    open(new_file, "w") as dest_file
                ):
                    data = origin.read()
                    dest_file.write(data)
            else:
                if not path.exists(dest):
                    makedirs(dest)
                with (
                    open(origin_file, "r") as origin,
                    open(path.join(dest, new_file), "w") as dest_file
                ):
                    data = origin.read()
                    dest_file.write(data)
            remove(origin_file)
