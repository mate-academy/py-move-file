from os import remove, path, mkdir


def move_file(command: str) -> None:
    command = command.split(" ")
    if len(command) != 3 or command[0] != "mv":
        return
    _, source, dest = command
    if source == dest:
        return
    try:
        dest_parts = dest.split("/")
        dir_parts = dest_parts[:-1]
        if dir_parts:
            cur = dir_parts[0]
            if cur != "" and not path.exists(cur):
                mkdir(cur)
            for part in dir_parts[1:]:
                cur = path.join(cur, part)
                if not path.exists(cur):
                    mkdir(cur)
        with open(source, "r") as src_file, open(dest, "w") as dest_file:
            dest_file.write(src_file.read())
        remove(source)
    except FileNotFoundError:
        return
