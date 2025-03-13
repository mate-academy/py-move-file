from os import mkdir, path, remove


def move_file(command: str) -> None:
    if command.startswith("mv") and len(command.split()) == 3:
        source, target = command.split()[1:]

        if path.dirname(target):
            path_folders = path.dirname(target).split("/")
            for i in range(len(path_folders)):
                path_temp = path.join(*path_folders[:i + 1])
                if not path.exists(path_temp):
                    mkdir(path_temp)

        if command.endswith("/"):
            target += source

        with (
            open(source, "r") as source_file,
            open(target, "w") as target_file
        ):
            target_file.write(source_file.read())

        remove(source)
