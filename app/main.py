from os import mkdir, remove


def move_file(command: str) -> None:

    parts = command.split()
    instr = parts[0]
    src = parts[1]
    dst = parts[2]
    sorce_file_name = src.split("/")[-1]

    if instr == "mv":
        if len(parts) == 3:
            if dst.endswith("/"):
                final_dst = dst + sorce_file_name
                create_dir(dst)
                with open(src, "r") as souce:
                    with open(final_dst, "w") as dest:
                        dest.write(souce.read())
                remove(src)
            else:
                create_dir(dst)
                with open(src, "r") as souce:
                    with open(dst, "w") as dest:
                        dest.write(souce.read())
                remove(src)


def create_dir(dst: str) -> None:

    paths = dst.split("/")[0:-1]
    current = ""
    for path in paths:
        if not path:
            continue
        if not current:
            current = path
        elif current:
            current += "/" + path
        try:
            mkdir(current)
        except (FileExistsError):
            continue
