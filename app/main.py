import os


def move_file(command: str) -> None:
    command = command.split()
    if command[0] == "mv":
        source_file, destination_path = command[1:]
        if "/" in destination_path:
            list_path = destination_path.split("/")
            list_path.pop(-1)
            path = ""
            for folder in list_path:
                path += os.path.join(f"{folder}/")
                if not os.path.exists(path):
                    os.mkdir(path)
        with (
            open(source_file, "r") as source,
            open(destination_path, "w") as new_file
        ):
            new_file.write(source.read())
        os.remove(source_file)
